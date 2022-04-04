import cv2 
print (cv2.__version__)
img = cv2.impread("resources\marriage.jpg")
#show image

cv2.imshow('Example - Show image in window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



