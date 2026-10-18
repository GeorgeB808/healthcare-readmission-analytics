import pandas as pd

file_path = "data/raw/IDS_mapping.csv"

df = pd.read_csv(file_path)

print("\n===== MAPPING DATASET OVERVIEW =====")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== COMPLETE MAPPING DATA =====")
print(df.to_string(index=False))

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())