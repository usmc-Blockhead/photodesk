from pil import *
import os

path = './images'
pathOut = './edited_images'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename")
    
    edit - img.filter(ImageFilter.SHARPEN).rotate(-90)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')