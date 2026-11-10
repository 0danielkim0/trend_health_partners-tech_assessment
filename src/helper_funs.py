from pathlib import Path
import requests
import sqlite3
import pandas as pd

# For log messages (diagnostics are always helpful and preferred)
import logging
import sys
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

###############
# Minor code & functions
###############

# Create log file for each run
LOG_DIR = Path("logs").mkdir(exist_ok = True)
timestamp = datetime.now().strftime("%Y%b%d_%H%M%S")
log_file = BASE_DIR/"logs"/f"Run-{timestamp}.txt"
sys.stdout = open(log_file, "w", buffering = 1)

###############
# Extract
###############

def download_tsv(
    github_url,
    output_file="./input/raw/source.csv",
    chunk_size=5000
):
    # Set constants
    total_rows = 0
    output_path = Path(output_file)
    output_path.parent.mkdir(parents = True, exist_ok = True)

    # Download is large, rely on .tmp file first
    input_files = output_path.with_suffix(".tmp")

    # Make sure download is manageable and link is working
    try:
        response = requests.get(
            github_url,
            stream=True,
            timeout=60
        )
        response.raise_for_status()
        print()
        
        # Stream download to temp file created before
        temp_tsv = input_files.with_suffix(".tsv")

        # Read file in parts at a time, keep from overwhelming local connection
        # This would likely be unnecessary when instead running a cluster for a stored table
        with open(temp_tsv, "wb") as f:
            for chunk in response.iter_content(1024 * 1024):
                if chunk:
                    f.write(chunk)

        # Parse TSV and convert to CSV in chunks
        for chunk in pd.read_csv(
            temp_tsv,
            sep="\t",
            dtype=str,
            chunksize=chunk_size
        ):
            # Load into Pandas, overwriting and appending as necessary
            chunk.to_csv(
                input_files,
                index=False,
                mode="w" if total_rows == 0 else "a",
                header=(total_rows == 0)
            )
            total_rows += len(chunk)

        # Set new file; will overwrite old file of same name
        input_files.replace(output_path)

        # Always preferred to have diagnostic messages
        print(f"Downloaded {total_rows:,} rows.")
        print(f"Saved to {output_path}")

    # Make sure directory is clean even if extraction fails
    finally:
        if input_files.exists():
            input_files.unlink()

        if 'temp_tsv' in locals() and temp_tsv.exists():
            temp_tsv.unlink()

###############
# Load
###############

def insert_table(
    df: pd.DataFrame,
    table_name: str
):
    # Set constants
    DB_PATH = BASE_DIR/"database"/"schema.db"
    SCHEMA_PATH = BASE_DIR/"database"/"schema.sql"
    
    # Execute within schema setup
    with sqlite3.connect(DB_PATH) as connection:

            # Get schema.sql file
            with open(SCHEMA_PATH, "r", encoding = "utf-8") as f:
                connection.executescript(f.read())

            # Insert dataframe into SQLite
            df.to_sql(
                name = table_name,
                con = connection,
                if_exists = "replace",
                index = False
            )

            print(f"Successfully inserted data into {table_name}")

###############
# Transform
###############

"""
    Refer to comments in main.py step 3.
"""