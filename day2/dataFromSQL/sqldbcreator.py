import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "students.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    subject TEXT,
    score INTEGER
)
""")

data = [
    ("Ravi", "Math", 85),
    ("Sam", "Math", 92),
    ("Nisha", "Physics", 78),
    ("Aarav", "Chemistry", 88)
]

cursor.executemany(
    "INSERT INTO marks (name, subject, score) VALUES (?, ?, ?)",
    data
)

conn.commit()
conn.close()

print(f"Database created at: {db_path}")

