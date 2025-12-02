import os
import sqlite3
import pandas as pd

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "students.db")

print("Using DB at:", db_path)

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM marks", conn)
print(df)
conn.close()
