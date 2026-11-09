-- ==========================================
-- TABLE: clue_data
-- One record per Jeopardy clue, not per air date (episode)
-- ==========================================

CREATE TABLE IF NOT EXISTS clue_data (
    clue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    air_date TEXT NOT NULL,
    round INTEGER NOT NULL
        CHECK (round IN (1, 2, 3)),
    clue_value INTEGER,
    daily_double_value INTEGER NOT NULL DEFAULT 0,
    category TEXT,
    comments TEXT,
    answer TEXT,
    question TEXT,
    notes TEXT,
    
	CHECK (
        date(air_date) IS NOT NULL
        AND date(air_date) = air_date
        AND air_date >= '2000-01-01'
    )
);

CREATE INDEX IF NOT EXISTS clue_id_date
ON clue_data(air_date);
CREATE INDEX IF NOT EXISTS clue_id_category
ON clue_data(category);
CREATE INDEX IF NOT EXISTS clue_id_round
ON clue_data(round);


-- ==========================================
-- TABLE: contest_data
-- One record per air date (single episode)
-- ==========================================

CREATE TABLE IF NOT EXISTS contest_data (
    contest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    air_date TEXT NOT NULL UNIQUE,
    season INTEGER NOT NULL
        CHECK (season BETWEEN 1 AND 42),
    name_left TEXT,
    name_middle TEXT,
    name_right TEXT,
    single_left INTEGER,
    single_middle INTEGER,
    single_right INTEGER,
    double_left INTEGER,
    double_middle INTEGER,
    double_right INTEGER,
    final_left INTEGER,
    final_middle INTEGER,
    final_right INTEGER,
    coryat_left INTEGER,
    coryat_middle INTEGER,
    coryat_right INTEGER,
    correct_left INTEGER,
    correct_middle INTEGER,
    correct_right INTEGER,
    wrong_left INTEGER,
    wrong_middle INTEGER,
    wrong_right INTEGER,

    CHECK (
        date(air_date) IS NOT NULL
        AND date(air_date) = air_date
        AND air_date >= '2000-01-01'
    )
);

CREATE INDEX IF NOT EXISTS contest_id_season
ON contest_data(season);