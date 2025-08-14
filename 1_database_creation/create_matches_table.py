import sqlite3
from init_db import db_path

'''
List color-agnostic features first, then white->black
You can't say "winner before lose" because some games have a draw, and also because that could get extra complicated from a coding standpoint
'''


CREATE_MATCHES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS matches (
    game_id             TEXT PRIMARY KEY,
    url                 TEXT,
    time_control        TEXT,
    timing_class        TEXT,
    winner_uuid         TEXT,
    winner_username     TEXT,

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
# "REAL" data type in SQL is the same as "FLOAT" in Python



conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute(CREATE_MATCHES_TABLE_SQL)
conn.commit()
conn.close()

print(f"✅ 'matches' table with proper field order created in {db_path}")
