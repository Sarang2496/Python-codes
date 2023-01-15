# editing images 

# for importing library
from PIL import Image # from PIL lobrary import class Image 
#from Pillow import Image
# import PIL

img = Image.open("3242948119.png")  # name of the object 
print (img.format)
area = (10, 10, 119, 133) # from the image wew need these figures

cropped_img = img.crop(area) # crop function is used
cropped_img.show()
# img.show()
print (img.size) # property or attribute
