import pandas as pd
from pathlib import Path

# Find the project root (one level above the python folder)
project_root = Path(__file__).resolve().parent.parent

# File locations
input_file = project_root / "data" / "raw" / "IDS_mapping.csv"
output_folder = project_root / "data" / "cleaned"

# Create cleaned folder if it doesn't exist
output_folder.mkdir(parents=True, exist_ok=True)

# Read the raw mapping file
df = pd.read_csv(input_file, header=None)

# Find section headers
admission_start = df[df[0] == "admission_type_id"].index[0]
discharge_start = df[df[0] == "discharge_disposition_id"].index[0]
source_start = df[df[0] == "admission_source_id"].index[0]

# Extract Admission Type mappings
admission_type = df.iloc[admission_start + 1:discharge_start].copy()
admission_type.columns = [
    "admission_type_id",
    "admission_type_description"
]

# Extract Discharge Disposition mappings
discharge = df.iloc[discharge_start + 1:source_start].copy()
discharge.columns = [
    "discharge_disposition_id",
    "discharge_disposition_description"
]

# Extract Admission Source mappings
source = df.iloc[source_start + 1:].copy()
source.columns = [
    "admission_source_id",
    "admission_source_description"
]

# Remove completely empty rows
admission_type = admission_type.dropna(how="all")
discharge = discharge.dropna(how="all")
source = source.dropna(how="all")

# Remove rows where the ID is not numeric
admission_type = admission_type[
    pd.to_numeric(admission_type["admission_type_id"], errors="coerce").notna()
]

discharge = discharge[
    pd.to_numeric(discharge["discharge_disposition_id"], errors="coerce").notna()
]

source = source[
    pd.to_numeric(source["admission_source_id"], errors="coerce").notna()
]

# Convert IDs to integers
admission_type["admission_type_id"] = (
    pd.to_numeric(admission_type["admission_type_id"]).astype(int)
)

discharge["discharge_disposition_id"] = (
    pd.to_numeric(discharge["discharge_disposition_id"]).astype(int)
)

source["admission_source_id"] = (
    pd.to_numeric(source["admission_source_id"]).astype(int)
)

# Save cleaned lookup tables
admission_type.to_csv(
    output_folder / "admission_type.csv",
    index=False
)

discharge.to_csv(
    output_folder / "discharge_disposition.csv",
    index=False
)

source.to_csv(
    output_folder / "admission_source.csv",
    index=False
)

print("Mapping tables created successfully.")
print()
print(f"Admission Type rows: {len(admission_type)}")
print(f"Discharge Disposition rows: {len(discharge)}")
print(f"Admission Source rows: {len(source)}")
print()
print("Files created:")
print(output_folder / "admission_type.csv")
print(output_folder / "discharge_disposition.csv")
print(output_folder / "admission_source.csv")