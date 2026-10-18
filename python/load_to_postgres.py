from pathlib import Path
import csv
import psycopg

# Project paths
project_root = Path(__file__).resolve().parent.parent
csv_file = project_root / "data" / "cleaned" / "diabetic_data_cleaned.csv"

# PostgreSQL connection
conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="healthcare_analytics",
    user="postgres",
    password=input("Enter PostgreSQL password: ")
)

print(f"Loading: {csv_file}")

with conn:
    with conn.cursor() as cur:

        # Clear staging table
        cur.execute("TRUNCATE TABLE encounters_staging;")

        # Load CSV directly into PostgreSQL
        with open(csv_file, "r", encoding="utf-8", newline="") as f:
            with cur.copy("""
                COPY encounters_staging
                FROM STDIN
                WITH (
                    FORMAT CSV,
                    HEADER TRUE,
                    DELIMITER ',',
                    QUOTE '"',
                    ESCAPE '"'
                )
            """) as copy:
                while data := f.read(1024 * 1024):
                    copy.write(data)

        # Verify row count
        cur.execute("SELECT COUNT(*) FROM encounters_staging;")
        row_count = cur.fetchone()[0]

        print(f"\nRows loaded: {row_count:,}")

print("\nPostgreSQL load complete.")