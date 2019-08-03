#!/usr/bin/env python

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
from pdf2image import convert_from_path
import cv2
import numpy as np
import argparse
from os import listdir
from os.path import isfile, join
FolderName = 'P1/'

FileList = [f for f in listdir(FolderName) if isfile(join(FolderName, f))]
print(FileList)

def main():
	# Parse Command Line arguments
    for idx in range(len(FileList)):
        #print('Saving File:'  + idx)
        print(idx)

        Parser = argparse.ArgumentParser()
	    FileName = FileList[idx][:-4] # Remove .pdf from the list
        Parser.add_argument('--PDFPath',
         default= FolderName+FileName+'.pdf',
         help = 'Path to read pdf from, Default: /home/')
        Parser.add_argument('--SavePath',
         default=FolderName+'Images/',
         help = 'Path to save image to, Default: /home/chahatdeep/Downloads/A.jpg')
        Args = Parser.parse_args()
        
        PDFPath = Args.PDFPath
        SavePath = Args.SavePath
    #    SavePath = [StudentName+'.jpg']

        pages = convert_from_path(PDFPath, 500)
        Scale = 0.125
        count = 1
        BorderWidth = 2

        for page in range(0, min([6, len(pages)])):
        	pages[page].save('temp.jpg', 'JPEG')
        	ImgNow = cv2.imread('temp.jpg')
        	Size = np.shape(ImgNow)

        	ImgNow = cv2.resize(ImgNow, (0,0), fx=Scale, fy=Scale)
        	BorderImgNow = cv2.copyMakeBorder(
    	                 ImgNow, 
    	                 BorderWidth, 
    	                 BorderWidth, 
    	                 BorderWidth, 
    	                 BorderWidth, 
    	                 cv2.BORDER_CONSTANT, 
    	                 value=[0,0,0])
        	if(count == 1):
        		ImgStacked = BorderImgNow
        	elif(count > 1):
        		ImgStacked = np.hstack((ImgStacked, BorderImgNow))

        	count += 1
            #print('Saved File:'+ idx + FileName)
        	cv2.imwrite(FolderName+'Images/'+FileName+'.jpg', ImgStacked)

if __name__ == '__main__':
	main()
