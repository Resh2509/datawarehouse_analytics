from pathlib import Path
import pandas as pd

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "superstore.csv"

def extract_data():
    # Read the CSV file
    df = pd.read_csv(DATA_PATH, encoding="latin1")

    print(f"\nLoaded {len(df)} records.\n")

    print("=" * 60)
    print("COLUMN NAMES")
    print("=" * 60)

    for col in df.columns:
        print(col)

    return df

if __name__ == "__main__":
    df = extract_data()

    print("\nFirst 5 Rows:\n")
    print(df.head())