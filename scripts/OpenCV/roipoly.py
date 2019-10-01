import cv2
import numpy as np

img = cv2.imread('images/lena.jpg')
mask = np.zeros(img.shape[:2],dtype = 'uint8')

c = [194, 253, 293, 245]
r = [72, 14, 76, 125]

rc = np.array((c,r)).T

cv2.drawContours(mask,[rc],0,255,-1)
cv2.drawContours(img,[rc],0,255,2)
mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

res = np.hstack((img,mask))
cv2.imshow('Image', res)  
while True:
    k = cv2.waitKey(0) & 0xFF    # 0xFF? To get the lowest byte.
    if k == 27: 
    	break            # Code for the ESC key

cv2.destroyAllWindows()

# To use mouse information, use cv2.setMouseCallback()
# To make border outside the image, use cv2.copyMakeBorder()

