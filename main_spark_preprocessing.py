import os
import logging
from pyspark.sql import SparkSession
from spark_pipeline.spark_preprocess import normalize_udf
import nltk

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Download NLTK assets if not already present
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

# Set environment variables
os.environ["PYSPARK_PYTHON"] = r"C:\My Projects\BA_Reviews_Sentiment_App\BA_venv\Scripts\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\My Projects\BA_Reviews_Sentiment_App\BA_venv\Scripts\python.exe"
os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ['JAVA_HOME'] = "C:\\Program Files\\Java\\jdk-1.8"

print("\n[DEBUG] Current Working Directory:", os.getcwd())
print("[DEBUG] Listing C:\\tmp:")
print(os.listdir("C:\\tmp") if os.path.exists("C:\\tmp") else "❌ C:\\tmp does not exist")
print("[DEBUG] Listing C:\\tmp\\hive:")
print(os.listdir("C:\\tmp\\hive") if os.path.exists("C:\\tmp\\hive") else "❌ C:\\tmp\\hive does not exist")

# Paths
data_path = os.path.join("data", "raw_reviews.csv")
final_output = os.path.join("data", "cleaned_reviews.csv")

if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ File not found: {data_path}")

try:
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Spark NLP Preprocessing") \
        .master("local[*]") \
        .config("spark.sql.warehouse.dir", "file:///C:/tmp/hive") \
        .config("spark.hadoop.hadoop.native.lib", "false") \
        .getOrCreate()

    print("[INFO] SparkSession started.")

    # Load data
    df = spark.read.csv(data_path, header=True)
    print(f"[INFO] Loaded {df.count()} records.")

    # Apply UDF
    df_clean = df.withColumn("cleaned_review", normalize_udf(df["reviews"]))
    df_clean.select("cleaned_review").show(5, truncate=100)

    # Save to CSV via pandas
    # df_clean.toPandas().to_csv(final_output, index=False)
    df_clean.select("cleaned_review").toPandas().to_csv(final_output, index=False)

    print(f"✅ Cleaned data saved to: {final_output}")

except Exception as e:
    print(f"❌ ERROR: {e}")




