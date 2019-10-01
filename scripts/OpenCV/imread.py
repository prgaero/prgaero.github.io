#!/usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt

# OPENCV reads BGR Image while Matplotlib follows RGB:
bgr_img = cv2.imread('images/lena.jpg')
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('images/lena_grayscale.jpg',gray_img)

plt.imshow(gray_img, cmap = plt.get_cmap('gray'))
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

while True:
    k = cv2.waitKey(0) & 0xFF    # 0xFF? To get the lowest byte.
    if k == 27: 
    	break            # Code for the ESC key

cv2.destroyAllWindows()