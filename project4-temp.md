---
layout: page
mathjax: true
title: Sexy Semantic Mapping
permalink: /2019/proj/p4-old/
---

Table of Contents:

- [1. Deadline](#due)
- [2. Introduction](#intro)
- [3. Extract object of interest from Table-Top Images](#table-top)
  - [3.1. Create a Point Cloud from RGB-D images](#create-pcl)  
  - [3.2. Build 3D model of object from RGB-D Images](#build-3D-model)
  - [3.3. Extract the ‘Collection of Objects’ from a given scene](#extract)
- [4. Segment the scene using known Objects](#segment)
- [5. Build a Semantic Map](#semantic)
- [6. Stuff Given to you](#stuff)
- [7. Notes about Test Set](#testset)
- [8. Submission Guidelines](#sub)
  - [8.1. File tree and naming](#files)
  - [8.2. Report](#report)
- [9. Collaboration Policy](#coll)
- [10. Acknowledgements](#ack)


<a name='due'></a>
## 1. Deadline 
**11:59PM, Monday, May 20, 2019.**


<a name='intro'></a>
## 2. Introduction

The aim of this project is to build semantic map of a 3D scene (See Fig. 1). This project gives you a peek into the world of robotics perception <i>i.e.</i> how robots understand and build the model of the world. <i>Excited?</i>

<div class="fig fighighlight"><center>
  <img src="/assets/2019/p4/seg.png" width="60%"></center>
  <div class="figcaption">
    Figure 1: (a) Reconstruction from a samples of RGBD images. (b) Segmentation of a 3D scene.
  </div>
  <div style="clear:both;"></div>
</div>


In the next few sections, we will detail how this can be done along with the specifications of the functions for each part. <b>Just like the previous projects, this project is to be done in groups of two and only one submission is required per group.</b>

<a name='table-top'></a>

## 3. Extract object of interest from Table-Top Images

You are given a set of RGB-D (RGB-Depth) frames of table top images and you need to extract the 'object of interest' from each frame and build a 3D model of the filtered object. When we say 'extract object of interest', you need to remove the table, walls of the room (if any) and any such irrelevant data from the scene. You also might need to filter stray points during the extraction process. But before that we need to align the data from RGB camera and the depth sensor from the Kinect. See Fig xx. Clearly, the RGB image and Depth images are not aligned. 

<div class="fig fighighlight">
  <img src="/assets/2019/p4/rgb.png" width="49%">
  <img src="/assets/2019/p4/depth.png" width="49%">
  <div class="figcaption">
  Figure 3 (a): RGB and Depth images from Kinect.
  </div>
  <br><center>
  <img src="/assets/2019/p4/rgbd.png" width="75%"></center>
  <div class="figcaption">
  Figure 3 (b): Uncalibrated RGB-D images. Thus we need calibration parameters in order to align the two images.
  </div>
  <div style="clear:both;"></div>
</div>

<a name='create-pcl'></a>

### 3.1. Create a Point Cloud from RGB-D images


So, in order to align them we would need calibration parameters <i>i.e.</i> the rotation and translation between the camera centers of RGB camera and the depth sensor as $$(u,v)$$ does not represents $$(u',v')$$, see fig. xx. 

<div class="fig fighighlight"><center>
  <img src="/assets/2019/p4/RotAndTrans1.png" width="90%"></center>
  <div class="figcaption">
    Figure 2: .
  </div>
  <div style="clear:both;"></div>
</div>

To formulate: Given all camera parameters $$(R,t,f)$$ (rotation, translation and focal lengths of both sensors), find the corresponding points of a RGB and a depth image. Thus, we need to generate a point cloud that can be represented as $$(x,y,z,r,g,b)$$. (See Fig. xx)
<div class="fig fighighlight"><center>
  <img src="/assets/2019/p4/RotAndTrans2.png" width="60%"></center>
  <div class="figcaption">
    Figure 2: .
  </div>
  <div style="clear:both;"></div>
</div>


In order to solve this problem, first recall: $$\cfrac{u}{f_u} = \cfrac{x}{z}$$
<p style="background-color:#ddd; padding:5px"><b>Note:</b>
Now, to generate a point cloud from RGB-D data, follow these steps:</p>
  - Compute 3D coordinate <font color="red">\(X^{IR}\)</font> in the <font color="red">\(IR\)</font> camera frame. (IR: Infrared or depth sensor frame)
  
<font color="red">\(x^{IR} = \cfrac{uz}{f^{IR}}\); \ \ \(y^{IR} = \cfrac{vz}{f^{IR}}\); \ \ \(X^{IR} = [x^{IR} \ y^{IR} \ z^{IR}]\)</font>
- Transform into RGB frame
  <font color="blue">\(X^{RGB} = RX^{IR} + t\)</font>
- Reproject them into the image plane
<font color="blue">\(u^{RGB} = f^{RGB}\cfrac{x^{RGB}}{z^{RGB}} = f^{RGB}\cfrac{y^{RGB}}{z^{RGB}}\)</font>
- Read <font color="blue">\((r,g,b)\)</font> at <font color="blue">\((u,v)^{RGB}\)</font>

  <font color="blue">\((r,g,b)\)</font> is the color of <font color="red">\(X^{IR}\)</font> point.
  
Now, once the point clouds are generated from a single view, let us learn how to build 3D model of the scene from multiple views.

<a name='build-3D-model'></a>

### 3.2. Build 3D model of object from RGB-D Images

The RGB-D data provided is recorded from an Asus Xtion Pro sensor. Using the method in the previous stage, you get the 3D view of the object from one single camera view point, use many such views from different frames of the same object to iteratively build a 3D model of the object.

<div class="fig fighighlight">
  <img src="/assets/2019/p4/data-collect.png" width="100%">
  <div class="figcaption">
    Figure 2: .
  </div>
  <div style="clear:both;"></div>
</div>


The idea here is you need to find out 3D translation and rotation parameters between two 3D point clouds of the same object from different frames, use these parameters to back project 3D point cloud from second frame on to the first and now you have little more information of the 3D model of the object as compared to the 3D point cloud from a single frame. You do it iteratively until you build a complete (or more or less complete) 3D model of the object.

You will need to implement any variant of the Iterative Closest Point (ICP) algorithm which gives the relative translation and rotation between two 3D point clouds. We have uploaded a lot of ICP related papers with this description for your reference, please cite the reference you follow.

<a name='extract'></a>

### 3.3. Extract the ‘Collection of Objects’ from a given scene

Here you will pretty much redo the same thing from previous sections, only difference being the set of table top images now have a collection of objects. And you need to extract just the objects without any irrelevant data from the scene.

<a name='segment'></a>

### 4. Segment the scene using known Objects

Now that you have reconstructed the 3D point cloud of the scene you need to segment each individual object of the scene by finding a suitable match in the set of 3D objects that you have already constructed. And while segmenting it you need to color code each object in the scene to the label of that object (feel free to use random color codes for each object such that each object is a different color). Also, note that you cannot assume that you know the number of objects in the scene, this has to be computed by your algorithm.

<a name='semantic'></a>

### 5. Build a Semantic Map

Now try to see if you can derive relationships between the segmented objects, like this object is at this angle with respect to another object or this object is so much smaller than another object or this object is on top of another object and so on. Think of this as modelling information how a human would think of this scene.

<a name='stuff'></a>

### 6. Stuff given to you

Calibration parameters and uncalibrated RGB-D data. Note that you are allowed to use third party code for basic stuff but not for the whole algorithm. You are only allowed to use `pcread`, `pcshow` from the Matlab’s point cloud library. Functions like `KDTreeSearcher` and `knnsearch` can be used for point to point correspondence search. You are also allowed to use any other basic functions built into the computer vision or image processing toolbox in Matlab.

Make sure to check Reference Papers folders for papers regarding ICP (Standard ICP paper is the easiest but the worst performing) and Object Segmentation. Dataset folder contains the data of various scenes containing individual objects and multiple objects.



<a name='testset'></a>
## 7. Notes about Test Set
One day (24 hours) before the deadline, a test set will be released with details of what faces to replace. We'll grade on the completion of the project and visually appealing results.

<a name='sub'></a>
## 8. Submission Guidelines


Make a video of all the objects and all the segmented scenes where you pan the 3D point cloud to show it is fully reconstructed and is correctly segmented for each object. You MUST submit a report written in IEEE double column format in L A TEXand should not exceed 6 pages (Template given in Draft folder). The report should be of a conference paper quality. Feel free to add videos you feel are cool or paste YouTube links in your report. You should also include a detailed README file explaining how to run your code.

Submit your .fig files (of 3D point clouds for all individual objects), codes (.m files) with the naming convention YourDirectoryID P5.zip onto ELMS/Canvas (Please compress it to .zip and no other format). If your e-mail ID is `ABCD[at]terpmail.umd.edu` or `ABCD[at]umd.edu` your Directory ID will be `ABCD`.

To summarize, you need to submit these things and in the following strcture: A zip file with the name `YourDirectoryID_P4.zip` onto ELMS/Canvas. A main folder with the name `YourDirectoryID_P4` with the following things (for EACH of the given scene)):

- A video showing a full 3D reconstruction for each object.
- A video showing a full 3D reconstruction and segmentation of each scene.
- <b>`.fig`</b> files for 3D models of all individual objects and scenes (color coded with segmentation labels)
- Code used for this project with a detailed README file.
- A conference paper quality report written in IEEE double column format in LATEX format (Check <b>`Draft`</b> folder for necessary template and class files)

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit </b>

<a name='files'></a>
### 8.1. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``YourDirectoryID_p3.zip``. If you email ID is ``abc@umd.edu`` or ``abc@terpmail.umd.edu``, then your ``DirectoryID`` is ``abc``. For our example, the submission file should be named ``abc_p1.zip``. The file **must have the following directory structure** because we'll be autograding assignments. The file to run for your project should be called ``Wrapper.py``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission.

```
YourDirectoryID_hw1.zip
│   README.md
|   Your Code files 
|   ├── Any subfolders you want along with files
|   Wrapper.py 
|   Data
|   ├── Data1.mp4
|   ├── Data2.mp4
|   ├── Data1OutputTri.mp4
|   ├── Data1OutputTPS.mp4
|   ├── Data1OutputPRNet.mp4
|   ├── Data2OutputTri.mp4
|   ├── Data2OutputTPS.mp4
|   ├── Data2OutputPRNet.mp4
└── Report.pdf
```
<a name='report'></a>
### 8.2. Report

For each section of the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented.  You must include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder and should of a conference quality paper.
- Present the Data you collected in ``Data`` folder with names ``Data1.mp4`` and ``Data2.mp4`` (Be sure to have the format as ``.mp4`` **ONLY**).
- Present the output videos for Triangulation, TPS and PRNet as ``Data1OutputTri.mp4``, ``Data1OutputTPS.mp4`` and ``Data1OutputPRNet.mp4`` for Data 1 respectively in the ``Data`` folder. Also, present outputs videos for Triangulation, TPS and PRNet as ``Data2OutputTri.mp4``, ``Data2OutputTPS.mp4`` and ``Data2OutputPRNet.mp4`` for Data 2 respectively in the ``Data`` folder. (Be sure to have the format as ``.mp4`` **ONLY**).
- For Phase 1, present input and output images for two frames from each of the videos using both Triangulation and TPS approach.
- For Phase 2, present input and output images for two frames from each of the videos using PRNet approach.
- Present failure cases for both Phase 1 and 2 and present your thoughts on why the failure occurred. 

<a name='coll'></a>
### 9. Collaboration Policy

You can discuss the ideas with any number of people. But the code you turn-in should be from your own team and you SHOULD NOT USE codes from other students. For other honor code refer to the CMSC733 Spring 2019 website.


<a name='ack'></a>
### 10. Acknowledgements

We would like to thank [Aleksandrs Ecins](http://users.umiacs.umd.edu/~aecins/) for the dataset. This fun project was inspired from Nitin’s research and a course project at University of Pennsylvania, [GRASP ARCHE](http://www.grasparche.com/).

