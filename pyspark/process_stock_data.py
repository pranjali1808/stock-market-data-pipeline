from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month

print("Starting Spark session...")

spark = SparkSession.builder.appName("StockMarketAnalysis").getOrCreate()

print("Loading cleaned dataset...")

df = spark.read.csv(
"data/cleaned/sp500_cleaned.csv",
header=True,
inferSchema=True
)

print("Dataset preview:")
df.show(5)

# Add new columns
df = df.withColumn("year", year("date"))
df = df.withColumn("month", month("date"))

print("Dataset with new columns:")
df.show(5)

spark.stop()

print("PySpark processing completed")