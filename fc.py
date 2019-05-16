from PIL import Image
import os

flist = os.listdir()

for a in flist:
    if a.endswith('.jpg'):
        im = Image.open(a)
        width, height = im.size
        im.close()
        if height > width:
            os.remove(a)
            
        

