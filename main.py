import os
from pdf2image import convert_from_path 
path="/home/ds/Documents/cit1/"    #  <--- change path here
filenames = next(os.walk(path))[2]
for f in filenames:
    #print(path)
    images = convert_from_path(path+f)
    name=(str(f).replace(".pdf", ""))
    for i in range(len(images)):
   
        # Save pages as images in the pdf
        images[i].save( name+str(i)+'.jpg', 'JPEG')
