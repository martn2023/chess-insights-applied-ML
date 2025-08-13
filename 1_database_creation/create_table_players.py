import sqlite3
import os
from init_db import db_path

# SQL CODE TO INJECT
CREATE_PLAYERS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS players (
    uuid        INTEGER PRIMARY KEY,
    username    TEXT UNIQUE NOT NULL,
    elo         INTEGER,
    title       TEXT
);
"""
 
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(CREATE_PLAYERS_TABLE_SQL)

conn.commit()
conn.close()

print(f"✅ 'players' table created in {db_path}")
