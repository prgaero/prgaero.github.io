---
layout: page
mathjax: true
title: Stereo Visual Odometry
permalink: /2019/proj/p4a/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
- [3. Implementation](#implementation)
	- [3.1. ROS Nodes](#rosnodes)
	- [3.2. Launch File](#launch)
	- [3.3. Rviz visualization](#rviz)
	- [3.4. Tag Detection](#tagdetection)
	- [3.5. Ellipse Fitting](#ellipsefit)
	- [3.6. Tag Pose](#pose)
- [4. Testing](#test)
- [5. Submission Guidelines](#sub)
  - [5.1. Report](#report)
  - [5.2. File tree and naming](#files)
- [6. Debugging Tips](#debug)
- [7. Allowed and Disallowed functions](#allowed)
- [8. Hardware Tips](#hw)
	- [8.1. Duo3D Camera Driver](#duo)
	- [8.2. Camera Calibration](#calibration)
- [9. Collaboration Policy](#coll)

<a name='due'></a>
## 1. Deadline 
**11:59PM, Tuesday, November 12, 2019** for submission of the report and video.

<a name='intro'></a>
## 2. Problem Statement
In this project, your aim is to compute the 3D camera poses of a stereo sensor. Imagine your stereo sensor - DUO Camera is on a quadrotor facing downwards. You can assume that the ground that the camera sees is <b>planar</b>. You need to collect data as a ROS bag/video while moving the sensor manually by hand or by flying the PRG Husky platform. You can use the carpets in lab IRB 0108. Feel free to change the illumination of the room. Define the coordinates as $$(0, 0, 0)$$ as the starting pose (the first frame). 

<a name='implementation'></a>
## 3. Implementation
You'll need to implement the following:

<a name='rosnodes'></a>
### 3.1. ROS Nodes
You need to create multiple ROS nodes to run your algorithm: one for pose estimation, another for filtering or one which does both. You can have any number of nodes as you desire.

<a name='launch'></a>
### 3.2. Launch File
All the above ROS nodes must be called using a single `launch` file.

<a name='rviz'></a>
### 3.3. Rviz visualization
You are required to plot the 3D camera pose on the ground (you can assume the center of the tag as the world frame origin) in `rviz` and plot you the PRG Husky pose relative to the tag using rviz tf like you did in the previous projects. A sample video for an april tag is shown [here](https://www.youtube.com/watch?v=rLcJFse74X4). Feel free to use the display code base from [here](https://github.com/berndpfrommer/tagslam_viz) and modify it to meet your needs.

<a name='tagdetection'></a>
### 3.4. Tag Detection
Detect the tag using any binarization method (thresholding), knowing that the tag is black on a white background. The tag is made of a filled circle in the center and 3 concentric thick rings around it all filled in black. To enable easy detection the tags have a white border around them. The tag from different viewpoints is shown in Fig. 2. Notice that the tag is glossy and has reflections. We recommend that you print the tag on A4 paper for your testing (make sure to not scale in an uneven fashion) so that the actual tag which you'll be testing on remains pristine.

<div class="fig fighighlight">
  <img src="/assets/2019/p3/CircularTag2.png" width="80%">
  <div class="figcaption">
    Figure 2: Circular bullseye target from different viewpoints.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='ellipsefit'></a>
### 3.5. Ellipse Fitting
Once the tag candidates have been detected, you should robustify your results by throwing out false detections. You can use any ellipse fitting method to do this. 

<a name='pose'></a>
### 3.6. Tag Pose
Once the tag has been detected, you'll need to recover the camera pose with respect to the tag. Here we assume that the tag is fixed and the camera is moving, hence the tag is in some known co-ordinates in an arbitrarily chosen world frame. The choice of the world frame could be as simple as the center of the tag as origin. Implement your own function or method to recover camera pose from the tag detection. Be sure to explain in detail with equations how you do this step in your report.

<a name='test'></a>
## 4. Testing
On the day of the deadline, each team will be given a 10 minute slot for demoing their code in action to the instructors.

Specifically, the team will place their PRG Husky at the corner of the flying space and then the instructors will place the circular bull's eye tag at $$(X,Y)$$ relative to the PRG Husky initial position with a covariance $$\Sigma$$. Your task is to take off, adjust your position according to the position of tag and then land on the tag.

**The tag is glossy and the camera will suffer from glares and reflection. So, your algorithm has to take into that account.**

<a name='sub'></a>
## 5. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit </b>

<a name='report'></a>
### 5.1. Report

Explain in detail your approach to complete the project, and describe any interesting problems you encountered and/or solutions you implemented.  You **MUST** include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder (Use the same draft folder from P1) and should of a conference quality paper.
- Present the output videos for trajectory following along with the 3D bullseye center position estimates in real-time as ``Outputs/Bullseye.mp4``.
- Tag detection (plotted on the image plane) in every frame as seen from Duo camera: `Bullseye-duo.mp4`. You can use any one or both the downfacing camera(s) from DUO.  
- Tag detection (3D pose) plotted in `rviz`: `Bullseye-rviz.mp4`. You are required to plot the circular bull's eye [image](assets/2019/p3/CircularTag.png) on the ground (you can assume the center of the tag as the world frame origin) in `rviz` and plot you the PRG Husky pose relative to the tag using rviz tf like you did in the previous projects. A sample video for an april tag is shown [here](https://www.youtube.com/watch?v=rLcJFse74X4). Feel free to use the display code base from [here](https://github.com/berndpfrommer/tagslam_viz) and modify it to meet your needs.

<a name='files'></a>
### 5.2. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``TeamYourTeamNumber_p3b.zip``. If you email ID is ``1``, then the submission file should be named ``Team1_p3b.zip``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission.

```
TeamYourTeamNumber_p3a.zip
│   README.md
|   Your Code files 
|   ├── Any subfolders you want along with files 
|   Outputs
|   ├──  Bullseye-duo.mp4
|   ├──  Bullseye-rviz.mp
|   └──  Bullseye.mp4
└── Report.pdf
```

<a name='debug'></a>
## 6. Debugging Tips
- To verify if your detections are working correctly, plot the circles/ellipses detected or pose of the tag on the image.

<a name='allowed'></a>
## 7. Allowed and Disallowed functions

<b> Allowed:

Any functions regarding reading, writing and displaying/plotting images and windows in `cv2`, `matplotlib`, `ROS`.
- Basic math utilities including convolution operations in `numpy` and `math`.
- Any functions for pretty plots.
- ``bebop_autonomy`` packages for controlling the PRGHusky.
- Hough Circles and `cv2.fitellipse` or any other function for contour fitting.

<b> Disallowed:
- Any function that directly estimates the pose of the ellipse in 3D.

<a name='hw'></a>
## 8. Hardware Tips

<a name='duo'></a>
### 8.1. Duo3D Camera Driver
Follow the steps from [this repo](https://github.com/NitinJSanket/Duo3D-Setup) to install the Duo3D camera driver.

<a name='calibration'></a>
### 8.2. Camera Calibration
The Duo3D camera comes calibrated out of the factory and gives only the calibrated images. To calibrate the extrinsics between the Duo3D stereo camera and front facing leopard imaging camera use the [Kalibr](https://github.com/ethz-asl/kalibr/wiki/camera-imu-calibration) package from ETH-Z and calibrate using the IMU from the Duo and the front camera since there is no common field of view between the two cameras to calibrate them directly. 


<a name='coll'></a>
## 9. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own team's, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the ENAE788M Fall 2019 website.
