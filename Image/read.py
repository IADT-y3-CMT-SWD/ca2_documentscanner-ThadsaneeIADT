#opening an image

import cv2 as cv 

img = cv.imread('Photos/puppy.jpg')

cv.imshow('Puppy', img)

cv.waitKey(0) #press any button
