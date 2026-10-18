import pandas as pd

# Load the raw healthcare dataset
file_path = "data/raw/diabetic_data.csv"

df = pd.read_csv(file_path)

print("\n===== DATASET OVERVIEW =====")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\n===== READMISSION DISTRIBUTION =====")
print(df["readmitted"].value_counts())

print("\n===== READMISSION PERCENTAGES =====")
print((df["readmitted"].value_counts(normalize=True) * 100).round(2))

print("\n===== UNIQUE PATIENTS =====")
print(f"Unique patients: {df['patient_nbr'].nunique():,}")

print("\n===== UNIQUE ENCOUNTERS =====")
print(f"Unique encounters: {df['encounter_id'].nunique():,}")

print("\n===== DUPLICATE ENCOUNTER IDs =====")
duplicates = df["encounter_id"].duplicated().sum()
print(f"Duplicate encounter IDs: {duplicates:,}")

print("\n===== MISSING VALUES =====")
missing = df.isnull().sum()
missing_percent = (df.isnull().mean() * 100).round(2)

missing_summary = pd.DataFrame({
    "Missing Values": missing,
    "Missing %": missing_percent
})

print(
    missing_summary[missing_summary["Missing Values"] > 0]
    .sort_values("Missing Values", ascending=False)
)

print("\n===== DATA TYPES =====")
print(df.dtypes)