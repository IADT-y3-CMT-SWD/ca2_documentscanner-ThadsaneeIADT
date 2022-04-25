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
import numpy as np

#Utility functions for document scanner
##############################
#trackbar code
def nothing(x):
    pass

# function to initialize Trackbars
def initializeTrackbars(intialTracbarVal=125):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Threshold1", "Trackbars", intialTracbarVal,255, nothing)
    cv2.createTrackbar("Threshold2", "Trackbars", intialTracbarVal, 255, nothing)
 
def valTrackbars():
    Threshold1 = cv2.getTrackbarPos("Threshold1", "Trackbars")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "Trackbars")
    src = Threshold1,Threshold2
    return src

#find biggest countour
def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    #loop through countours list
    for i in contours:
        area = cv2.contourArea(i)
        #discard areas below treshold
        if area > 5000:
            #calculates a contour perimeter -> float
            peri = cv2.arcLength(i, True)
            #calcualtes a curve or a polygon with another curve/polygon with less vertices
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            # print(f'Area: {area}, Peri: {peri}, Approx: {approx}')
            # is it a rectangle?
            if area > max_area and len(approx) == 4:
                biggest = approx
                #overwrite max_area for regions that are lareger
                max_area = area
    return biggest,max_area
 
#reordering points in order to warp image
def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = myPoints.sum(1)
 
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] =myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    
    return myPointsNew   
 
def drawRectangle(img,biggest,thickness):
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 155, 0), thickness)
    cv2.line(img, (biggest[0][0][0], biggest[0][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 155, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[2][0][0], biggest[2][0][1]), (0, 155, 0), thickness)
    cv2.line(img, (biggest[3][0][0], biggest[3][0][1]), (biggest[1][0][0], biggest[1][0][1]), (0, 155, 0), thickness)
 
    return img

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

blr_img = cv2.blur(img, (15,15))

imshow('Blurred image', blr_img) #show the blured image 
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

#cropping img 

img = imread('Image/pup.jpg') #reading an image 
crop_img = img[0:400,100:400]#cropping image from x,y,w,h = 100, 200,300,400

imshow('Cropped image',crop_img) #show the cropped image 
waitKey(0) #waits till key is pressed
destroyAllWindows() #destroy teh window 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#mix image

#path to input images are specified 
image1 = imread('Image/image 1.jpg')
image2 = imread('Image/image 2.jpg')

#cv.2addWeighted is applied over the image input with applied parameters 
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4,0)

#the window shows the output image
#with the weighted sum 
imshow('Weighted image',weightedSum)

#de allocate associated memory usage
if waitKey(0) & 0xff ==27:
    destroyAllWindows()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#subtract image 1 and 2

#cv.2subtract is applie over the image inouts with the applied parameters 
sub = cv2.subtract(image1, image2)

#shows output image with the subtract image 
imshow('Subtracted image', sub)

#de-allocate associated memory usage
if waitKey(0) & 0xff ==27:
    destroyAllWindows()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#draw the line 
#draws 3 thick red pixels line from the top right corner to bottom left 

red = (0,0,255)
cv2.line(img, (300,0), (9,300),red,3)

#draw a rectangle with 5 pixel thick  
cv2.rectangle(img,(50,200), (200,255),red,5)
blue = (255,0,0)
cv2.rectangle(img,(50,200), (200,255),blue,-1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~









