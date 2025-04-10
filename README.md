# ✈️ British Airways Review Analyser — Sentiment & Rating with LLM

This end-to-end NLP project takes user reviews of British Airways, cleans them using Spark, analyzes them with LLM models, predicts sentiment and rating, and displays results through both Kafka-streamed CLI and a beautiful Gradio-based web app!

---

## 🚀 Project Highlights

- ✅ **Web Scraping**: Reviews scraped from British Airways website.
- ✅ **Data Cleaning**: Preprocessing with custom NLTK pipeline using Spark UDF.
- ✅ **ETL Process**: Extract → Clean (Transform) → Predict (Load).
- ✅ **Real-Time Streaming**: Kafka-based pipeline for live reviews and CLI predictions.
- ✅ **LLM Model Integration**: Used Hugging Face Transformers for rating and sentiment.
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
