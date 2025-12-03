import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sensor_readings.csv")

df = pd.read_csv(csv_path)
print(df)
