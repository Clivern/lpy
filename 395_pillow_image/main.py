# 395. Pillow images
#
# PIL.Image.new creates an image. save writes PNG or JPEG. size is (width, height). resize
# and crop return new images. Pixel access is load() or numpy.
#
# Run: python 395_pillow_image/main.py

from PIL import Image
from io import BytesIO
im = Image.new("RGB", (8, 4), (255, 0, 0))
buf = BytesIO()
im.save(buf, format="PNG")
print(im.size, im.mode, buf.tell() > 0)
