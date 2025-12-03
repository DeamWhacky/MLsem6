import os
import json
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "data.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

students = data["students"]
df = pd.DataFrame(students)

print(df)
