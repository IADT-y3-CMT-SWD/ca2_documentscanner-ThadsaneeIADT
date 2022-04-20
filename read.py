#opening an image

import cv2
print(cv2.__version__)

img = cv2.imread('Image/pup.jpg')

cv2.imshow('Puppy', img) #show the image

cv2.waitKey(0) #press any button
cv2.destroyAllWindows()

#reading videos 


