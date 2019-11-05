import cv2
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags
import numpy as np

# cap = cv2.VideoCapture(0)

# Take each frame
frame = cv2.imread('images/lena.jpg')

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

while True:
    k = cv2.waitKey(0) & 0xFF    # 0xFF? To get the lowest byte.
    if k == 27: 
    	break            # Code for the ESC key

cv2.destroyAllWindows()