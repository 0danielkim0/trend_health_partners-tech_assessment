# Packages

from pathlib import Path
import pandas as pd
import csv
import papermill as pm

# Helper functions
from src.helper_funs import *

# Base information

BASE_DIR = Path(__file__).resolve().parent

clue_url = "https://raw.githubusercontent.com/jwolle1/jeopardy_clue_dataset/refs/heads/main/combined_season1-42.tsv"
contest_url = "https://raw.githubusercontent.com/jwolle1/jeopardy_clue_dataset/refs/heads/main/other_data/scoring_season1-42.tsv"

print("Pipeline started.")

# 1. Read in data
print("--- 1. Read in data ---")

clue_df = download_tsv(
    clue_url,
    output_file="./input/raw/clue.csv",
    chunk_size=5000
)

contest_df = download_tsv(
    contest_url,
    output_file="./input/raw/contest.csv",
    chunk_size=5000
)

# 2. Insert downloaded data into SQLite
print("--- 2. Insert downloaded data into SQLite ---")

insert_table(
    df = pd.read_csv(BASE_DIR/"input"/"raw"/"clue.csv"),
    table_name = "clue_data"
)

insert_table(
    df = pd.read_csv(BASE_DIR/"input"/"raw"/"contest.csv"),
    table_name = "contest_data"
)

# 3. Transform tables
print("--- 3. Transform tables ---")
print("Transformation step skipped.")

"""
    Note: Some tables do not require major transformation, especially with a well-laid out 'schema.sql' file. The 'schema.sql' file is most important for laying out explicit column types, given that many production pipelines break most frequently due to mistyped values.

    Note: The pipeline orders stages as "ELT" rather than "ETL" for three reasons:

        1. Production pipelines will not always have a fully transform-capable data source to pull from.

        2. Even with a transform-capable data source, oftentimes needing to run extra computations within the main data source can take up valuable memory and time. Of course, this is case-by-case depending on the computation limits of both sides and the amount of data being run through. (This pipeline, for example, is both small and straightforward. A pipeline with gigabytes per column will need better models.)

        3. Later schemas can be altered freely when the source data is immutable and holistic.
"""

# 4. Run IPYNB file
print("--- 4. Run IPYNB file ---")

NB_IN_PATH = BASE_DIR/"notebooks"/"analysis.ipynb"
NB_OUT_PATH = BASE_DIR/"notebooks"/"analysis_output.ipynb" 

pm.execute_notebook(NB_IN_PATH, NB_OUT_PATH)

print("Refer to ./notebooks/analysis_output.ipynb for pipeline's main output.")
print("Pipeline now complete.")