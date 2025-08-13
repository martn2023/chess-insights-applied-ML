import os
import sqlite3


# SQLite db file should NOT be in this folder, should be one level up in the root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(project_root, "chess_insights.sqlite")


conn = sqlite3.connect(db_path)
conn.close()

print(f"✅ Empty database created at: {db_path}")
