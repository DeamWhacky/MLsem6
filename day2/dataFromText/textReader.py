import os

script_dir = os.path.dirname(os.path.abspath(__file__))
txt_path = os.path.join(script_dir, "sample.txt")

with open(txt_path, "r", encoding="utf-8") as f:
    text = f.read()

print(text)
