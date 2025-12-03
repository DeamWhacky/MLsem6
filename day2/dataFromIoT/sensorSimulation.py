import os
import time
import random
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sensor_readings.csv")

with open(csv_path, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temperature_c"])

    for _ in range(5):
        ts = int(time.time())
        temp = round(random.uniform(20.0, 35.0), 2)
        writer.writerow([ts, temp])
        print(f"{ts} -> {temp} °C")
        time.sleep(1)

print(f"Sensor data written to: {csv_path}")
