from PIL import Image
import numpy as np
import math

img = Image.open("input.jpeg").convert("RGBA")
arr = np.array(img)
rotation = math.radians(90)
out = np.zeros_like(arr)

for butie_x in range(360):
    for butie_y in range(360):
        arr_img_storage = arr[butie_y, butie_x]
        callicurated_x = math.cos(rotation)*butie_x-math.sin(rotation)*butie_y
        callicurated_y= -math.sin(rotation)*butie_x+math.cos(rotation)*butie_y
        x2 = int(round(callicurated_x))
        y2 = int(round(callicurated_y))
        out[y2,x2] = arr_img_storage

Image.fromarray(out).save("output.png")