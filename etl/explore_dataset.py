import pandas as pd

# Load dataset
df = pd.read_csv("data/superstore.csv", encoding="latin1")

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe(include="all"))