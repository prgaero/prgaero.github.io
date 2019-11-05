#!/usr/bin/env python

import cv2  
image_path = 'images/lena.jpg'
image = cv2.imread(image_path) 

# Window name in which image is displayed 
window_name = 'Image'

# Represents top left corner:
start_point = (0, 0) 
end_point = (250, 250) 

# BGR
color = (0, 255, 0) 
thickness = 9

radius = 20
row, col = 20,100
thickness_circle = -1
#thickness_circle = 1
image = cv2.line(image, start_point, end_point, color, thickness) 
cv2.circle(image,(row, col), 50, (0,255,0), thickness_circle)
cv2.imshow(window_name, image)  
while True:
    k = cv2.waitKey(0) & 0xFF    # 0xFF? To get the lowest byte.
    if k == 27: 
    	break            # Code for the ESC key

cv2.destroyAllWindows()
# Go through these: cv2.rectangle(), cv2.ellipse(), cv2.putText()

