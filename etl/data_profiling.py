from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "superstore.csv"

df = pd.read_csv(DATA_PATH, encoding="latin1")

print("=" * 80)
print("DATASET PROFILE")
print("=" * 80)

print(f"\nRows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn Names:")
for col in df.columns:
    print(f"- {col}")

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Values:")
print(df.nunique())

print("\nFirst 5 Rows:")
print(df.head())