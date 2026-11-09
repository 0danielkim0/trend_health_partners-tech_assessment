# Packages

import pandas as pd
import csv
import pipe

# Raw access

clue_url = "https://raw.githubusercontent.com/jwolle1/jeopardy_clue_dataset/refs/heads/main/combined_season1-42.tsv"
contest_url = 
"https://raw.githubusercontent.com/jwolle1/jeopardy_clue_dataset/refs/heads/main/other_data/scoring_season1-42.tsv"

# 1. Read in data

df = pd.read_csv(
    url,
    sep="\t",
    dtype=str,
    chunksize=5000
) |
    to_csv('output.csv', index = False)


print("Download complete.")