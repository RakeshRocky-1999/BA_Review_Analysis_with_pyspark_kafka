# ✈️ British Airways Review Analyser — Sentiment & Rating with LLM

This project is an end-to-end NLP pipeline that performs sentiment analysis and rating prediction (1 to 5 stars) on customer reviews for British Airways using Spark, Kafka, and a Hugging Face Transformer (BERT LLM model). The system cleans the text data, processes it using a Spark pipeline, streams live reviews through Kafka, and delivers predictions in real time. The final deployment is hosted using Gradio for public interaction.

---

## 🚀 Project Highlights

- ✅ **Web Scraping**: Reviews scraped from British Airways website.
- ✅ **Data Cleaning**: Preprocessing with custom NLTK pipeline using Spark UDF.
- ✅ **ETL Process**: Extract → Clean (Transform) → Predict (Load).
- ✅ **Real-Time Streaming**: Kafka-based pipeline for live reviews and CLI predictions.
- ✅ **LLM Model Integration**: Used Hugging Face Transformers(BERT) for rating and sentiment.
- ✅ **Deployment**: Frontend deployed on Hugging Face Spaces via Gradio UI.

---

## 📁 Project Structure

```bash
├── requirements.txt
├── main_spark_preprocessing.py             # Spark UDF ETL pipeline
├── llm_model/
│   └── sentiment_analysis.py               # LLM-based rating + sentiment
├── spark_pipeline/
│   └── spark_preprocess.py                 # Spark UDF for text cleaning
├── kafka_consumer.py                       # Consumes reviews, predicts
├── kafka_producer.py                       # Sends reviews to Kafka topic
├── Notebooks/
│   ├── Discovering Insights from British Airways Reviews Using AI and NLP.ipynb
│   └── Web_Scrapping_Reviews_British_Airways_website.ipynb
├── data/
│   ├── raw_reviews.csv
│   ├── cleaned_reviews.csv
│   ├── raw_data_prediction.csv
│   └── kafka_predicted_reviews.csv

```

## 🔄 ETL Pipeline Overview

graph TD

**A**[📝 Raw Reviews] **--> B**[🔄 Spark Preprocessing]

**B --> C**[📦 Cleaned Data CSV]

**C --> D**[🧠 LLM Model Prediction]

**D --> E**[📊 Rating & Sentiment Output]


### 🟢 Extract
- Scraped reviews from British Airways website using `BeautifulSoup` and `requests`.

### 🟡 Transform
- Applied Spark-based preprocessing:
  - Custom UDF: stopword removal, contraction expansion, lemmatization, and Unicode normalization.
  - Removed irrelevant phrases like "Trip Verified", digits, and special characters.
- Streamed live reviews via **Kafka producer**, processed in real-time by **Kafka consumer**.

### 🔵 Load
- Batch cleaned data saved to `data/cleaned_reviews.csv`.
- Real-time predictions stored in `data/kafka_predicted_reviews.csv`.
- Final sentiment and rating outputs stored in `data/final_predictions.csv`.

📡 **Kafka Flow**:



