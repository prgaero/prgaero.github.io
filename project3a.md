---
layout: page
mathjax: true
title: Mini Drone Race 
permalink: /2019/proj/p3a/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
- [3. Window Statistics](#window)
- [4. Implementation](#implementation)
  - [4.1 ROS Nodes](#node)
  - [4.2 Launch File](#launch)
  - [4.3 Rviz visualization](#rviz)
  - [4.4 Color Segmentation](#seg)
    - [4.4.1 Color Segmentation Using Thresholding](#thresh)
    - [4.4.2 Color Segmentation Using Single Gaussian](#gauss)
    - [4.4.3 Color Segmentation Using a Gaussian Mixture Model (GMM)](#gmm)
    - [4.4.4 Line/Shape Fitting](#fit)
    - [4.4.5 Final Filtering](#filter)
- [5. Test Set](#test)
- [6. Live Demo](#live)
- [7. Submission Guidelines](#sub)
  - [7.1. Report](#report)
  - [7.2. File tree and naming](#files)
- [8. Debugging Tips](#debug)
- [9. Allowed and Disallowed functions](#allowed)
- [10. Collaboration Policy](#coll)

<a name='due'></a>
## 1. Deadline 
**11:59PM, Thursday, October 17, 2019** for submission of the report and video.

<a name='intro'></a>
## 2. Problem Statement
In this project, your aim is to navigate through a colored window (Fig. 1) of known size but unknown position and orientation. Windows of two different colors (yellow and purple) are setup in the lab IRB 0108. You need to collect data as a ROS bag/video capture while moving the monocular camera pointed at different angles and different illumination of the window (sample images are shown in Fig. 2). Feel free to place the windows at any distance and orientation you desire for your testing. You'll need to implement the detection algorithm of windows using color or edges or whatever you desire. Note that you'll have to calibrate the camera to estimate the value of the camera matrix $$K$$. Also, you'll need to rectify the images before processing them. Once you've estimated the window pose in 3D, implement a trajectory planner and control algorithm to go through the window. 

<div class="fig fighighlight">
  <img src="/assets/2019/p3/GapFlyt.png" width="80%">
  <div class="figcaption">
    Figure 1: Three colored windows placed behind each other (random position and orinentation). The aim is to fly through the windows as fast as possible.
  </div>
  <div style="clear:both;"></div>
</div>


<div class="fig fighighlight">
  <img src="/assets/2019/p3/Windows.png" width="100%">
  <div class="figcaption">
    Figure 2: The same window looks very different under different orientation and lighting/illumination settings.
  </div>
  <div style="clear:both;"></div>
</div>

<a name='window'></a>
## 3. Window Statistics

The window measures (length and breadth) are shown in the figure 3. Note that the height of the windows are unknown. Also, the windows may or may not be exactly rectangular as shown in the figure 3. The windows are made of white PVC pipes of diamemer 6.2 cm and are spray pained in yellow and or violet.

<div class="fig fighighlight">
  <img src="/assets/2019/p3/Windows2.png" width="80%">
  <div class="figcaption">
    Figure 3: Window dimensions.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='implementation'></a>
## 4. Implementation

The instructors will place the quadrotor and the window at a certain orientation and position, making sure that the part of the window is visible in the first frame on take off. Your job is to detect the window and go through. There will be ONLY one window and that can be of either yellow or purple (you will informed only a minute before flying) and of some arbitrary height. You need to implement the following:

<a name='node'></a>
### 4.1 ROS Nodes
You need to create multiple ROS nodes to run your algorithm: one for vision, another for the control or one which does both. You can have any number of nodes as you desire.

<a name='launch'></a>
### 4.2 Launch File
All the above ROS nodes must be called using a single `launch` file.

<a name='rviz'></a>
### 4.3 Rviz visualization
You need to plot the window in `rviz` along with the trajectory (and pose i.e. both position and orientation) of your quadrotor. The `rviz` visualization must show the correct color: either purple or yellow. A sample visualization is shown in Fig. 4. Be sure to fix your window in some arbitrarily chosen world frame and plot your camera's (quadrotor's) pose with respect to it.

<div class="fig fighighlight">
  <img src="/assets/2019/p3/windowRviz.gif" width="80%">
  <div class="figcaption">
    Figure 4: Rviz Visualization of the detected windows.
  </div>
  <div style="clear:both;"></div>
</div>

<a name='seg'></a>
### 4.4 Color Segmentation

<a name='thresh'></a>
#### 4.4.1 Color Segmentation Using Thresholding

Implement color thresholding without using any built-in or third party code for color thresholding. Include your outputs (as a video) for the Test set. Feel free to use any color space you desire, you can use built-in or third party code for color conversions.

<a name='gauss'></a>
#### 4.4.2 Color Segmentation Using Single Gaussian

Implement color thresholding without using any built-in or third party code for color segmentation using a single gaussian. Include your outputs (as a video) for the Test set. Feel free to use any color space you desire, you can use built-in or third party code for color conversions and dataset labelling. 

<a name='gmm'></a>
#### 4.4.3 Color Segmentation Using a Gaussian Mixture Model (GMM)

Implement color thresholding without using any built-in or third party code for color segmentation using a GMM (use more than 1 gaussian).  Include your outputs (as a video) for the Test set. Feel free to use any color space you desire, you can use built-in or third party code for color conversions and dataset labelling. 

<a name='fit'></a>
#### 4.4.4 Line/Shape Fitting

Implement an algorithm to fit a line to the detected color without using any built-in or  third party code. You are allowed to use code for linear and non-linear optimizers, however any piece of code which fits a line directly is not allowed.

<a name='filter'></a>
#### 4.4.5 Final Filtering

Use any built-in and third party morphoplogical operation for this.

_Be sure to cite any third party code you use._

<a name='test'></a>
## 5. Test Set
A test set will be released 24 hours before the deadline. The test set will either be in the form of a ROS bag or a mp4 video showing one of the colored windows from different orientation, position and illumination. You have to output the detected corners of the window overlayed on each frame and export this to an mp4 video which you need to include in your report. You also need to display the pose the camera with respect to the window as numbers overlayed on the same video (please define your coordinate axes and origin in your report so we can make sense of your numbers).

<a name='live'></a>
## 6. Live Demo
On the day of the deadline, each team will be given a 15 minute slot for demonstrating their code in action to the instructors. The instructors will place the windows as well as the PRG Husky quadrotor as they wish (position, orientation and choice of colored window at different heights). The instructors will make sure that atleast a part of the window is in the visible region as seen from the first frame (note that it is not guarenteed that the complete window will be visible in the first frame). The task is the fly through the windows as fast as possible. You also need to show us a live visualization of your detection (corners of the window overlaid on the image) along with the 3D visualization of the window with the relative camera pose overlaid in rviz.


<a name='sub'></a>
## 7. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit </b>

<a name='report'></a>
### 7.1. Report

Explain in detail your approach to complete the project, and describe any interesting problems you encountered and/or solutions you implemented.  You **MUST** include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder (Use the same draft folder from P1) and should of a conference quality paper.
- Present Vicon plots for each trajectory followed along with the estimated 3D window position overlaid on the same plot. (Show all three views ``X-Y``, ``X-Z`` and ``Y-Z``).
- Present the output videos for trajectory following along with the window estimates in real-time as ``Outputs/GapFlyt.mp4``. Be sure to use appropriate colors to plot the windows in ``rviz``, for eg., blue color for a blue window and so on.


<a name='files'></a>
### 7.2. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``TeamYourTeamNumber_p3a.zip``. If you email ID is ``1``, then the submission file should be named ``Team1_p3a.zip``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission.

```
TeamYourTeamNumber_p3a.zip
│   README.md
|   Your Code files 
|   ├── Any subfolders you want along with files 
|   Outputs
|   └──  GapFlyt.mp4
└── Report.pdf
```

<a name='debug'></a>
## 8. Debugging Tips
- To verify if your detections are working correctly, plot the corners of the window on the image, they should align with the true window corners. 
- To verify if your pose estimation is correct, re-project the estimated 3D corners of the window onto the image. They should be very close to the detected corners.

<a name='allowed'></a>
## 9. Allowed and Disallowed functions

<b> Allowed:

Any functions regarding reading, writing and displaying/plotting images and windows in `cv2`, `matplotlib`, `ROS`.
- Basic math utilities including convolution operations in `numpy` and `math`.
- Any functions for pretty plots.
- ``bebop_autonomy`` packages for controlling the PRGHusky.
- Functions for color thresholding including GMM.
- Functions for line fitting and corner detection.


<b> Disallowed:
- Any function that implements trajectory interpolation.
- Any function that directly detects the window.


<a name='coll'></a>
## 10. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own team's, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the ENAE788M Fall 2019 website.
