"""
Caitlin Locke
Code in Place
Final Project
5.25.2020
"""

"""
File: triptych.py
----------------
Take an original image. Crop it into three parts. Create a new 
image that is 20 pixels wider than the original image. Place 
cropped images into new image as a triptych.
"""

# The lines below import SimpleImage and Image
from simpleimage import SimpleImage
from PIL import Image

#Create image constrants, so the original image can be easily changed
USER_DIRECTORY = 'images/'
#The image must be a JPEG for this code to work
IMAGE = 'images/quad.jpg'
IMAGE_NAME = 'quad'

def main():
    """
    This program creates a triptych from an original image. Constants
    allow the user to pick an image of their choice and turn it into a
    triptych.
    """
    original = SimpleImage(IMAGE)
    original.show()
    image_crop(IMAGE)
    triptych = make_triptych(IMAGE)
    triptych.show()

#Creates triptych from original image
def make_triptych(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height
    #Creates new image to contain triptych
    triptych = SimpleImage.blank(width + 20, height)
    #Creates panel one of triptych
    image = SimpleImage(USER_DIRECTORY + IMAGE_NAME + '_1.JPG')
    width1 = image.width
    height1 = image.height
    for y in range(height1):
        for x in range(width1):
            pixel = image.get_pixel(x,y)
            triptych.set_pixel(x,y,pixel)
    #Creates panel two of triptych
    image = SimpleImage(USER_DIRECTORY + IMAGE_NAME + '_2.JPG')
    width2 = image.width
    height2 = image.height
    for y in range(height2):
        for x in range(width2):
            pixel = image.get_pixel(x, y)
            triptych.set_pixel(x + ((width/4) + 10), y, pixel)
    #Creates panel three of triptych
    image = SimpleImage(USER_DIRECTORY + IMAGE_NAME + '_3.JPG')
    width3 = image.width
    height3 = image.height
    for y in range(height3):
        for x in range(width3):
            pixel = image.get_pixel(x, y)
            triptych.set_pixel(x + (((width/4)*3) + 20), y, pixel)
    return triptych

#Crops original image into three parts for triptych
def image_crop(filename):
    im_name = IMAGE_NAME
    im = Image.open(filename)
    width = im.width
    height = im.height
    #crops first panel
    im1 = im.crop((0, 0, width/4, height))
    im1.save(USER_DIRECTORY + IMAGE_NAME + '_1.JPG')
    #crops second/middle panel
    im2 = im.crop((width/4, 0, (width/4) * 3, height))
    im2.save(USER_DIRECTORY + IMAGE_NAME + '_2.JPG')
    #crops third panel
    im3 = im.crop(((width/4) * 3, 0, width, height))
    im3.save(USER_DIRECTORY + IMAGE_NAME + '_3.JPG')

if __name__ == '__main__':
    main()
