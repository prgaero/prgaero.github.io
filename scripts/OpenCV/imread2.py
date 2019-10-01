import cv2
import numpy as np
import matplotlib.pyplot as plt

bgr_img = cv2.imread('images/lena.jpg')

b,g,r = cv2.split(bgr_img)       # get b,g,r
rgb_img = cv2.merge([r,g,b])     # switch it to rgb

plt.imshow(rgb_img)
plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
plt.show()

cv2.waitKey(5)

# while True:
#     k = cv2.waitKey(1)# & 0xFF    # 0xFF? To get the lowest byte.
#     if k == 27: break            # Code for the ESC key

cv2.destroyAllWindows()
