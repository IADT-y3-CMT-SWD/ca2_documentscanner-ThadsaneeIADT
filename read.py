#presenting image

from configparser import Interpolation
from tkinter import Frame
import cv2
from cv2 import IMREAD_UNCHANGED
from cv2 import imread
from cv2 import IMREAD_GRAYSCALE
from cv2 import imshow 
from cv2 import imwrite 
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import resize

print(cv2.__version__)

img = imread('Image/pup.jpg') #reading an image 
imshow('Puppy', img) #show the image in a window

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Resizing Image
dsize = (200,400) #resize to truple dsize)
output = resize(img,dsize) #resizing the image

#show output
imshow('Puppy resize', output)
imwrite('output/pup.jpg',output)
waitKey(0) #waits till key is pressed
destroyAllWindows() #destroy teh window 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Blurring image

img_rst = cv2.blur(img, (15,15))

imshow('Blurring image',img_rst) #show the blured image 
waitKey(0) #waits till key is pressed
destroyAllWindows() #destroy teh window 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# i = imread("pup.jgp")
# i = imread("pup.jgp", IMREAD_UNCHANGED)
# i = imread("pup.jgp", IMREAD_GRAYSCALE)
# imshow("Title", i)
# imwrite("pup.jgp", i)
# waitKey(0)
# destroyAllWindows()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





