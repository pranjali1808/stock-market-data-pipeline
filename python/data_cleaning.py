import pandas as pd

print("Loading dataset...")

# load raw dataset
df = pd.read_csv("data/raw/sp500_prices.csv")

print("Original rows:", len(df))

# remove duplicates
df = df.drop_duplicates()

# remove missing values
df = df.dropna()

# convert date column
df["date"] = pd.to_datetime(df["date"])

print("Rows after cleaning:", len(df))

# save cleaned dataset
df.to_csv("data/cleaned/sp500_cleaned.csv", index=False)

print("Cleaned dataset saved successfully")