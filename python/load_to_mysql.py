import pandas as pd
import mysql.connector

print("Loading cleaned dataset...")

df = pd.read_csv("data/cleaned/sp500_cleaned.csv")

# keep only columns we need
df = df[['date','symbol','open','high','low','close','volume']]

print("Connecting to MySQL...")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="stock_market"
)

cursor = conn.cursor()

insert_query = """
INSERT INTO stock_prices
(date, symbol, open, high, low, close, volume)
VALUES (%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

conn.commit()

print("Data loaded successfully!")

cursor.close()
conn.close()