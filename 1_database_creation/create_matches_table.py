import sqlite3
from init_db import db_path

CREATE_MATCHES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS matches (
    game_id             TEXT PRIMARY KEY,
    url                 TEXT,
    time_control        TEXT,
    timing_class        TEXT,
    winner_uuid         TEXT,
    winner_username     TEXT,
    raw_pgn             TEXT,
    clean_pgn           TEXT,

    white_username      TEXT,
    white_elo_rating    INTEGER,
    white_opening       TEXT,
    white_accuracy      REAL,
    white_result        TEXT,

    black_username      TEXT,
    black_elo_rating    INTEGER,
    black_opening       TEXT,
    black_accuracy      REAL,
    black_result        TEXT
);
"""

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute(CREATE_MATCHES_TABLE_SQL)
conn.commit()
conn.close()

print(f"✅ 'matches' table with PGN fields created in {db_path}")
