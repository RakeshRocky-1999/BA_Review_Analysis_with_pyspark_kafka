# ✈️ British Airways Review Analyzer — Sentiment & Rating with LLM

This project is an end-to-end NLP pipeline that performs sentiment analysis and rating prediction (1 to 5 stars) on customer reviews for British Airways using Spark, Kafka, and a Hugging Face Transformer (BERT LLM model). The system cleans the text data, processes it using a Spark pipeline, streams live reviews through Kafka, and delivers predictions in real time. The final deployment is hosted using Gradio for public interaction.

---
![Spark](https://img.shields.io/badge/Spark-Enabled-orange?logo=apache-spark)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black?logo=apache-kafka)
![LLM](https://img.shields.io/badge/LLM-HuggingFace-yellow?logo=huggingface)
![Gradio](https://img.shields.io/badge/UI-Gradio-blue?logo=gradio)
![License](https://img.shields.io/badge/License-MIT-yellow)

🎥 **Demo Video**: [Watch the project demo here](https://drive.google.com/file/d/1HseD21BFZwxKPF2oHNf9ZQuSEDZPkRrJ/view?usp=sharing)

🌐 **Try it Live**: [Click here to access the deployed app](https://rakeshrocky-1999.github.io/Review_Analyser_Sentiment_Rating/)


![ReviewAnalyzer-Gif](https://github.com/user-attachments/assets/2a3b2468-9a84-43a2-8047-dc65f11cce7d)


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

## 🧠 Models Used
- `nlptown/bert-base-multilingual-uncased-sentiment` — ⭐ Rating (1 to 5)
- `Custom logic` — Maps ratings to sentiment (positive, neutral, negative)

## 📡 Kafka Live Prediction (CLI-based)
- 1. Producer accepts typed input
- 2. Kafka sends to consumer
- 3. Consumer cleans → predicts rating → derives sentiment

✅ Output seen instantly in terminal!

## 🌐 Web Deployment with Gradio
**The app allows users to:**

- Type their review ✍️

- See the cleaned version 🧼

- View sentiment with emoji and color 😊😐😠

- View a star-based rating ⭐⭐⭐⭐☆

**🔗 Live App:**
👉 [Try the Deployed Web App](https://rakeshrocky-1999.github.io/Review_Analyser_Sentiment_Rating/)

App

## 🧪 Try Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run Spark Preprocessing
python main_spark_preprocessing.py

# Run Sentiment & Rating Predictions
python llm_model/sentiment_analysis.py

# Start Kafka (ensure Zookeeper & broker are up)
python kafka_producer.py
python kafka_consumer.py

```

## 🛠 Tech Stack
- 🔥 PySpark
- 📦 Apache Kafka
- 🤗 Hugging Face Transformers
- ✨ Gradio + HTML Styling
- 🧹 NLTK, regex, contractions
- 📊 Pandas, tqdm
- 🤝 Author

## ✅ Conclusion

This project showcases a complete end-to-end pipeline—from data extraction to real-time prediction and deployment. By combining web scraping, Apache Spark, Kafka, custom NLP preprocessing, and LLM-based sentiment analysis, we built a powerful and scalable review analysis system.

**Key achievements:**

- ✅ Scraped over 4000 British Airways reviews for real data

- ✅ Built a robust Spark pipeline for preprocessing using custom NLP techniques

- ✅ Streamed live reviews using Kafka for real-time predictions

- ✅ Predicted both ratings and sentiments using state-of-the-art LLMs

- ✅ Developed a clean and responsive frontend using Gradio

- ✅ Deployed the app publicly on Hugging Face Spaces for easy accessibility

This project demonstrates not only technical implementation but also real-world applicability of a complete ETL + NLP + Deployment pipeline, suitable for production-grade sentiment analysis systems.
