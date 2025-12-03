import os
import time
import random
import csv
from datetime import datetime

# Folder where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "stream_events.csv")

events = ["login", "logout", "purchase", "error", "view_page"]

# Open CSV and write header
with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "event_type"])

    print("Simulating streaming events...\n")

    for _ in range(10):  # 10 fake events
        ts = datetime.now().isoformat(timespec="seconds")
        event = random.choice(events)

        # "Stream" output to console
        print(f"{ts} -> {event}")

        # Collect/store in CSV
        writer.writerow([ts, event])

        time.sleep(1)  # wait 1 second between events

print(f"\nEvents collected and saved to: {csv_path}")
