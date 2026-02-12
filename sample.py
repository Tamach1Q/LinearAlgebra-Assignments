from PIL import Image
import numpy as np
import math

img = Image.open("input.jpeg").convert("RGBA")
arr = np.array(img)

rotation = math.radians(90)
out = np.zeros_like(arr)

h, w = arr.shape[:2]
cx = (w - 1) / 2.0
cy = (h - 1) / 2.0

c = math.cos(rotation)
s = math.sin(rotation)

for butie_y in range(h):
    for butie_x in range(w):
        arr_img_storage = arr[butie_y, butie_x]

        x = butie_x - cx
        y = butie_y - cy

        callicurated_x = c * x - s * y + cx
        callicurated_y = s * x + c * y + cy

        x2 = int(round(callicurated_x))
        y2 = int(round(callicurated_y))

        if 0 <= x2 < w and 0 <= y2 < h:
            out[y2, x2] = arr_img_storage

Image.fromarray(out).save("output.png")