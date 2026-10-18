import pandas as pd
from pathlib import Path

# ============================================================
# PROJECT PATHS
# ============================================================

project_root = Path(__file__).resolve().parent.parent

raw_file = project_root / "data" / "raw" / "diabetic_data.csv"
cleaned_folder = project_root / "data" / "cleaned"
cleaned_file = cleaned_folder / "diabetic_data_cleaned.csv"

# Create cleaned folder if needed
cleaned_folder.mkdir(parents=True, exist_ok=True)


# ============================================================
# LOAD DATA
# ============================================================

print("Loading dataset...")

df = pd.read_csv(raw_file)

print(f"Original rows: {len(df):,}")
print(f"Original columns: {len(df.columns)}")


# ============================================================
# STANDARDIZE MISSING VALUES
# ============================================================

print("\nStandardizing missing values...")

df = df.replace("?", pd.NA)


# ============================================================
# AGE GROUP
# ============================================================

print("Creating age group...")

age_map = {
    "[0-10)": "0-9",
    "[10-20)": "10-19",
    "[20-30)": "20-29",
    "[30-40)": "30-39",
    "[40-50)": "40-49",
    "[50-60)": "50-59",
    "[60-70)": "60-69",
    "[70-80)": "70-79",
    "[80-90)": "80-89",
    "[90-100)": "90+"
}

df["age_group"] = df["age"].map(age_map)


# ============================================================
# READMISSION FLAGS
# ============================================================

print("Creating readmission indicators...")

# 30-day readmission
df["readmitted_30_days"] = (
    df["readmitted"] == "<30"
).astype(int)

# Any readmission
df["any_readmission"] = (
    df["readmitted"] != "NO"
).astype(int)


# ============================================================
# NUMERIC COLUMNS
# ============================================================

numeric_columns = [
    "encounter_id",
    "patient_nbr",
    "admission_type_id",
    "discharge_disposition_id",
    "admission_source_id",
    "time_in_hospital",
    "num_lab_procedures",
    "num_procedures",
    "num_medications",
    "number_outpatient",
    "number_emergency",
    "number_inpatient",
    "number_diagnoses"
]

print("Converting numeric fields...")

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# ============================================================
# ADMISSION TYPE MAPPING
# ============================================================

print("Applying admission type mapping...")

admission_file = cleaned_folder / "admission_type.csv"

admission_map = pd.read_csv(admission_file)

df = df.merge(
    admission_map,
    on="admission_type_id",
    how="left"
)


# ============================================================
# DISCHARGE DISPOSITION MAPPING
# ============================================================

print("Applying discharge disposition mapping...")

discharge_file = cleaned_folder / "discharge_disposition.csv"

discharge_map = pd.read_csv(discharge_file)

df = df.merge(
    discharge_map,
    on="discharge_disposition_id",
    how="left"
)


# ============================================================
# ADMISSION SOURCE MAPPING
# ============================================================

print("Applying admission source mapping...")

source_file = cleaned_folder / "admission_source.csv"

source_map = pd.read_csv(source_file)

df = df.merge(
    source_map,
    on="admission_source_id",
    how="left"
)


# ============================================================
# VERIFY ENCOUNTER IDs
# ============================================================

print("\nChecking encounter IDs...")

duplicate_encounters = df["encounter_id"].duplicated().sum()

print(
    f"Duplicate encounter IDs after cleaning: "
    f"{duplicate_encounters}"
)


# ============================================================
# VERIFY PATIENT COUNTS
# ============================================================

unique_patients = df["patient_nbr"].nunique()

print(
    f"Unique patients: {unique_patients:,}"
)


# ============================================================
# VERIFY READMISSION DISTRIBUTION
# ============================================================

print("\nReadmission distribution:")

print(
    df["readmitted"]
    .value_counts(dropna=False)
)


print("\n30-day readmission rate:")

readmission_rate = (
    df["readmitted_30_days"].mean() * 100
)

print(
    f"{readmission_rate:.2f}%"
)


# ============================================================
# SAVE CLEANED DATASET
# ============================================================

print("\nSaving cleaned dataset...")

df.to_csv(
    cleaned_file,
    index=False
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n===================================")
print("DATA CLEANING COMPLETE")
print("===================================")

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

print("\nCleaned dataset saved to:")

print(cleaned_file)