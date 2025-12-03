import os

script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "app.log")

errors = []

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if "ERROR" in line or "WARNING" in line:
            errors.append(line)

print("Errors / Warnings found:")
for e in errors:
    print(e)
