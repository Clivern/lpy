# 073. Pillow
#
# Create and save images.
#
# Run: python 073_pillow/main.py

from PIL import Image
from io import BytesIO
im = Image.new("RGB", (8, 4), (255, 0, 0))
buf = BytesIO()
im.save(buf, format="PNG")
print(im.size, im.mode, buf.tell() > 0)
