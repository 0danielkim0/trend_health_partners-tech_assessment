
# THP — Data Engineer II Technical Exercise

## Context

Recent research on the Coryat score, a Jeopardy performance-tracking system developed by Season 12 winner Paul Coryat, inspired the making of this project. ('Performance' here essentially measures knowledge, not money.)

**Coryat Score = Total dollar amount for correct responses - Total dollar amount for incorrect responses**

Note that:
- The wager for a Daily Double is not included. Instead, a correct response adds the listed dollar value, while an incorrect response leaves the score as is. This keeps the score "honest" and limited to trivia, without the added variable of betting.
- Final Jeopardy is excluded altogether, given the same reasoning as Daily Double where clues have no set value. Furthermore, Final Jeopardy can theoretically be repeated so long as the contestants continue the sudden-death.

## Setup

- Primary stack: Python 3 + SQLite
- Configuration
  - OS: Mac
  - Python version: 3.11.8
  - Pip version: 24.0
  - SQLite version: 3.45.1
- Package installation *(Note: Not all packages may be necessary, but this typically covers all bases for most general-use projects.)*
`pip install requests pandas beautifulsoup4 lxml python-dotenv pytest jupyter matplotlib`

Directory
- `database`: .sql files
- `docs`: reference materials
- `input`: data from Github
  - `raw`: downloaded file remains untouched
  - `processed`: copies of original file to clean
- `notebooks`: .ipynb files
- `output`: formatted results, processed visuals, knitted notebooks
- `tests`: automated tests

## Run Instructions

1. Make sure of configuration.
```
python 3 install
python3 --version
python -m pip install --upgrade pip
python3 -m pip --version
```
2. Open virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Run following code to download paginated data subset, perform tidying, and answer research questions.
`python main.py`

## Schema

[image here]

Note 1: normalization into dimension/fact tables was not applied in this case; the data (1) has too few potential ID columns, and (2) did not require anti-redundancy or significant write/update capability for a project this size.
Note 2: the pipeline does not implement record updating, instead replacing all files. A larger-scale enterprise setup would likely benefit from table-write operations in particular for raw data, to avoid overwhelming memory.

## Data

Note: only data with dates from January 01, 2000 onward are kept.

Table 1: `clue_data` *(Note: data dictionary for this table was copied from original data source)*

| Field | Description |
|---|---|
| `round` | 1 for Single Jeopardy, 2 for Double Jeopardy, or 3 for Final Jeopardy. |
| `clue_value` | The clue's value on the board before any Daily Double wagering. |
| `daily_double_value` | If the clue is a Daily Double, this is the amount wagered. Otherwise, it is zero. |
| `category` | The top row of the board. |
| `comments` | The host's comments about a category. |
| `answer` | The prompt given to contestants. |
| `question` | The correct response. |
| `air_date` | The calendar date on which the episode first aired. |
| `notes` | Miscellaneous information about the clue, e.g., if it's from a special tournament match. |

Table 2: `contest_data`

| Field | Description |
|---|---|
| `season` | The official season number, between 1 and 42 inclusive. |
| `air_date` | The calendar date on which the episode first aired. |
| `name_left` | Left participant's first and last name. |
| `name_middle` | Middle participant's first and last name. |
| `name_right` | Right participant's first and last name. |
| `single_left` | Left participant's score upon finishing Single Jeopardy round. |
| `single_middle` | Middle participant's score upon finishing Single Jeopardy round. |
| `single_right` | Right participant's score upon finishing Single Jeopardy round. |
| `double_left` | Left participant's score upon finishing Double Jeopardy round. |
| `double_middle` | Middle participant's score upon finishing Double Jeopardy round. |
| `double_right` | Right participant's score upon finishing Double Jeopardy round. |
| `final_left` | Left participant's score upon finishing Final Jeopardy round. |
| `final_middle` | Middle participant's score upon finishing Final Jeopardy round. |
| `final_right` | Right participant's score upon finishing Final Jeopardy round. |
| `coryat_left` | Coryat score for left participant upon finishing Double Jeopardy. |
| `coryat_middle` | Coryat score for middle participant upon finishing Double Jeopardy. |
| `coryat_right` | Coryat score for right participant upon finishing Double Jeopardy. |
| `correct_left` | Total correct responses from left participant upon completing Final Jeopardy. |
| `correct_middle` | Total correct responses from middle participant upon completing Final Jeopardy. |
| `correct_right` | Total correct responses from right participant upon completing Final Jeopardy. |
| `wrong_left` | Total incorrect responses from left participant upon completing Final Jeopardy. |
| `wrong_middle` | Total incorrect responses from middle participant upon completing Final Jeopardy. |
| `wrong_right` | Total incorrect responses from right participant upon completing Final Jeopardy. |

## Research Questions

1. A
2. B
3. C
4. D
5. E

## Sources / Licenses

Original dataset source: https://github.com/jwolle1/jeopardy_clue_dataset