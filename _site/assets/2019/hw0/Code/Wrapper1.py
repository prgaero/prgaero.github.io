#!/usr/bin/env python

"""
CMSC733 (Spring 2019): 
Homework Zero: Starter Code
"""

"""
Written by: Chahat Deep Singh (chahat@terpmail.umd.edu) 
PhD in CS stduent in University of Maryland, College Park
Adapted from Nitin J Sanket's Code from CMSC426 Project 1
"""

# Code starts here:

import numpy as np
import cv2

from sobel_pb import *
from canny_pb import *


"""
Generate Oriented Gaussian Filter Bank:
Display all the Gaussian Filter Bank and save image as GaussianFB_ImageName.png,
use command "cv2.imwrite('GaussianFB_ImageName', img)"
"""



"""
Generate Half-disk masks
Display all the GHalf-disk masks and save image as HDMasks_ImageName.png,
use command "cv2.imwrite('HDMasks_ImageName', img)"
"""



"""
Generate Texton Map
Filter image using oriented gaussian filter bank
"""



"""
Generate texture id's using K-means clustering
Display texton map and save image as TextonMap_ImageName.png,
use command "cv2.imwrite('TextonMap_ImageName', img)"
"""



"""
Generate Texton Gradient (tg)
Perform Chi-square calculation on Texton Map
Display tg and save image as tg_ImageName.png,
use command "cv2.imwrite('tg_ImageName', img)"
"""



"""
Generate Brightness Map
Perform brightness binning 
Display brightness map and save image as BrightnessMap_ImageName.png,
use command "cv2.imwrite('tg_ImageName', img)"
"""



"""
Generate Brightness Gradient (bg)
Perform Chi-square calculation on Brightness Map
Display bg and save image as bg_ImageName.png,
use command "cv2.imwrite('bg_ImageName', img)"
"""



"""
Get Sobel Baseline
Uncomment the bottom line
im is the grayscale version of the original image
DO NOT CHANGE THE VALUES IN THE FOLLOWING FUNCTION!!
SobelPb = sobel_pb(im,0.08:0.02:.3);
"""



"""
Display SobelPb and save image as SobelPb_ImageName.png
use command "cv2.imwrite('SobelPb_ImageName', img)"
"""



"""
Get Canny Baseline
Uncomment the bottom line
im is the grayscale version of the original image
DO NOT CHANGE THE VALUES IN THE FOLLOWING FUNCTION!!
CannyPb = canny_pb(im,0.1:0.1:.7,1:1:4);
"""



"""
Display CannyPb and save image as CannyPb_ImageName.png
use command "cv2.imwrite('CannyPb_ImageName', img)"
"""



"""
Combine responses to get pb-lite output
A simple combination function would be: PbLite = np.multiply((tg+gb), (SobelPb+CannyPb))
(Element-wise multiplication)

Display PbLite and save image as PbLite_ImageName.png
use command "cv2.imwrite('PbLitePb_ImageName', img)"
"""



