#!/usr/bin/env python

import sys
from pdf2image import convert_from_path
import cv2
import numpy as np
import argparse
import os
import glob
import zipfile
from fnmatch import fnmatch
from tqdm import tqdm


def ExtractPDFsAndConvertToImg(ZipFilePath, SavePath):
    zip = zipfile.ZipFile(ZipFilePath)
    BaseFolder = ZipFilePath.replace('.zip', '')
    zip.extractall(BaseFolder)
    
    for file in tqdm(glob.glob(BaseFolder+'/*.zip')):
        FileName = file.split('_')[0]
        FileName = FileName.split('/')[-1]
        zip = zipfile.ZipFile(file)
        FolderNow = file.replace('.zip', '')
        zip.extractall(BaseFolder+'/'+FileName+'/')
        print('Extracting done....')
        # Delete zip file
        os.remove(file)
        # Extract the Report.pdf out
        for path, subdirs, files in os.walk(BaseFolder+'/'+FileName+'/'):
            for name in files:
                if name == 'Report.pdf':
                    PDFFileNameNow = FileName
                    PDF2Img(path + '/' + name, PDFFileNameNow, SavePath)

def PDF2Img(PDFPath, FileName, SavePath):
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
        print('Page {} of {} complete'.format(page+1, min([6, len(pages)])))
    cv2.imwrite(SavePath+FileName+'.jpg', ImgStacked)
    print('Image Written....')


def main():
    Parser = argparse.ArgumentParser()
    # FileName = FileList[idx][:-4] # Remove .pdf from the list
    Parser.add_argument('--ZipFilePath',
     default= '/mnt/d/PhDInCS/Summer2019/ENAE788M/Grading/P1a.zip',
     help = 'Path to read pdf from, Default: /mnt/d/PhDInCS/Summer2019/ENAE788M/Grading/P1a.zip')
    Parser.add_argument('--SavePath',
     default='/mnt/d/PhDInCS/Summer2019/ENAE788M/Grading/P1aImgs/',
     help = 'Path to save image to, Default: /mnt/d/PhDInCS/Summer2019/ENAE788M/Grading/P1a/Imgs/')

    Args = Parser.parse_args()

    ZipFilePath = Args.ZipFilePath
    SavePath = Args.SavePath

    # Create SavePath if doesn't exist
    if not os.path.exists(SavePath):
        os.makedirs(SavePath) 

    ExtractPDFsAndConvertToImg(ZipFilePath, SavePath)

        

if __name__ == '__main__':
	main()