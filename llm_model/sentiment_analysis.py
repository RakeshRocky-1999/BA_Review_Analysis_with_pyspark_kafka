import os
import pandas as pd
from transformers import pipeline
import torch
from tqdm import tqdm
import re

# Paths
input_path = os.path.join("data", "cleaned_reviews.csv")
output_path = os.path.join("data", "raw_data_predictions.csv")

# Load and clean data
print("[INFO] Loading cleaned review dataset...")
df = pd.read_csv(input_path)
df = df[df["cleaned_review"].notna()]
df = df[df["cleaned_review"].str.strip() != ""]

print(f"[INFO] Loaded {len(df)} cleaned reviews.")

# Set device
device = 0 if torch.cuda.is_available() else -1
print(f"[INFO] Using {'GPU' if device == 0 else 'CPU'}")

# Load rating prediction model
print("[INFO] Loading Hugging Face rating prediction pipeline...")
rating_pipe = pipeline(
    "text-classification",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    tokenizer="nlptown/bert-base-multilingual-uncased-sentiment",
    device=device
)

# Add prediction columns
df["predicted_rating"] = 0
df["predicted_sentiment"] = ""

# Function to extract rating number from label (e.g., "5 stars" → 5)
def clean_rating_label(label):
    match = re.search(r"\d", label)
    return int(match.group()) if match else 0

# Function to convert rating to sentiment
def derive_sentiment_from_rating(rating):
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"

# Prediction loop
print("[INFO] Predicting ratings and deriving sentiments...\n")

for idx, row in tqdm(df.iterrows(), total=len(df)):
    review = row["cleaned_review"]
    try:
        rating_result = rating_pipe(review, truncation=True, max_length=512)[0]
        rating = clean_rating_label(rating_result["label"])
        sentiment = derive_sentiment_from_rating(rating)

        df.at[idx, "predicted_rating"] = rating
        df.at[idx, "predicted_sentiment"] = sentiment

        print(f"[{idx+1}/{len(df)}] ✅ Rating: {rating}, Sentiment: {sentiment} — Review: {review[:60]}...")

    except Exception as e:
        print(f"[{idx+1}] ⚠️ Error: {e}")
        df.at[idx, "predicted_rating"] = 0
        df.at[idx, "predicted_sentiment"] = "error"

# Save final predictions
df[["cleaned_review", "predicted_rating", "predicted_sentiment"]].to_csv(output_path, index=False)
print(f"\n✅ Final predictions saved to: {output_path}")

