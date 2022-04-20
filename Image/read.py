#opening an image

import cv2 as cv 

img = cv.imread('Scanned/puppy.jpg')

cv.imshow('Puppy', img)

cv.waitKey(0) #press any button
