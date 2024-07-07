from PIL import Image
import os
# Open an existing image
path = "G:\\codebase\\rpa\\images\\lines\\"
for val in os.listdir(path):
    print(val)
    
    image = Image.open(os.path.join(path,val))  # Change the path to your image file
    nm = os.path.join(path,val).split(".")[0]+'.tif'
    nm = nm.replace(" ","")
    # Save the image as a TIFF file
    image.save(nm)
