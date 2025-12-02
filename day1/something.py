import os
import pandas as pd

data = [
    {'name': 'Soumyadeep', 'branch': 'CSE', 'year': 3, 'cgpa': 8.98},
    {'name': 'Siddhart', 'branch': 'CSE', 'year': 3, 'cgpa': 9.1},
    {'name': 'Aveerup', 'branch': 'IT', 'year': 2, 'cgpa': 8.4},
    {'name': 'Bibek', 'branch': 'EE', 'year': 1, 'cgpa': 8.1},
    {'name': 'Sayantan', 'branch': 'ECE', 'year': 3, 'cgpa': 7.8},
    {'name': 'Sagnik', 'branch': 'ECE', 'year': 2, 'cgpa': 9.1}
]

df = pd.DataFrame(data)

script_dir = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(script_dir, "student_records.csv")

df.to_csv(csv_path, index=False)

print(f"CSV saved at: {csv_path}")
