import os
from PIL import Image

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "Everything.jpeg")

img = Image.open(img_path)
print("Format:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)


