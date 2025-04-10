import json
import pickle
import pandas as pd
import re
from kafka import KafkaConsumer
from transformers import pipeline
from pathlib import Path


# Get the cleaning pattern from the cleaned reviews
def mimic_cleaning(text: str) -> str:
    # Write logic based on what you applied in the cleaned_reviews.pkl
    text = re.sub(r"(Trip Verified|Not Verified)", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.lower()
    return text

# --- Load Rating Model ---
rating_pipe = pipeline(
    "text-classification",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
    tokenizer="nlptown/bert-base-multilingual-uncased-sentiment"
)

# --- Kafka Consumer ---
consumer = KafkaConsumer(
    "reviews",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

def get_sentiment_from_rating(rating: int) -> str:
    if rating >= 4:
        return "positive"
    elif rating == 3:
        return "neutral"
    else:
        return "negative"

def clean_rating_label(label: str) -> int:
    match = re.search(r"\d", label)
    return int(match.group()) if match else 0


results = []  

print("🚀 Listening for review messages...\n")

for message in consumer:
    raw_review = message.value.get("review_text", "")

    if not raw_review.strip():
        print("⚠️ Empty review received. Skipping...\n")
        continue

    try:
        cleaned_review = mimic_cleaning(raw_review)
        result = rating_pipe(cleaned_review)[0]
        rating = clean_rating_label(result["label"])
        sentiment = get_sentiment_from_rating(rating)

        print(f"🔍 Review: {raw_review[:60]}...")
        print(f"📊 Cleaned: {cleaned_review[:60]}...")
        print(f"✅ Rating: {rating}, Sentiment: {sentiment}\n")

        # ✅ Save prediction to results list
        results.append({
            "review": raw_review,
            "cleaned": cleaned_review,
            "rating": rating,
            "sentiment": sentiment
        })

        # ✅ Save to CSV after every new record (optional: reduce frequency)
        pd.DataFrame(results).to_csv("data/kafka_predicted_reviews.csv", index=False)

    except Exception as e:
        print(f"❌ Error processing review: {e}")
