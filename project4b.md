---
layout: page
mathjax: true
title: Avoid the wall and find the bridge
permalink: /2019/proj/p4b/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
- [3. Implementation](#implementation)
	- [3.1. ROS Nodes](#rosnodes)
	- [3.2. Launch File](#launch)
	- [3.3. Rviz visualization](#rviz)
- [4. Submission Guidelines](#sub)
  - [4.1. Report](#report)
  - [4.2. File tree and naming](#files)
- [5. Debugging Tips](#debug)
- [6. Allowed and Disallowed functions](#allowed)
- [7. Hardware Tips](#hw)
	- [7.1. Duo3D Camera Driver](#duo)
	- [7.2. Camera Calibration](#calibration)
- [8. Collaboration Policy](#coll)

<a name='due'></a>
## 1. Deadline 
**11:59PM, Tuesday, November 12, 2019** for submission of the report and video.

<a name='intro'></a>
## 2. Problem Statement
In this project, you have two tasks: <br>
<i>(i)</i> You need your quadrotor to cross over the bridge while avoiding the river.<br>
<i>(ii)</i> Detect the wall infront of your quadrotor and go through above or below the wall, depending on the height of the wall.<br>
Let's understand the problem statement in depth.

Your PRG Husky platform is equipped with a front facing RGB camera, a down facing stereo grayscale and an IMU. For the first task, you are in a space with a thin river-like band of blue sheet on the floor. Only a small region has a ladder/bridge on the top of the river. Your aim is to avoid the blue river and cross it above the bridge. But there's a catch, your bottom facing camera is grayscale. You need to detect textures of the river in order to avoid it. Or you can simply detect where the bridge is and go above it. Refer fig. 1.

<div class="fig fighighlight">
  <img src="/assets/2019/p4/river-ladder.png" width="80%">
  <div class="figcaption">
    Figure 1: Task 1 - A sample scene with bridge and river.
  </div>
  <div style="clear:both;"></div>
</div>


For your second task, you are given a wall of certain length and breadth which is placed at a some unknown distance infront of the PRG Husky. You are going to do some version of odometry/PnP to estimate the distance and position of the wall in some arbitrary units. To get it to metric scale, use the down-facing camera estimates which are in absolute or metric scale. Once you have estimated the position and the distance of the wall w.r.t. PRG Husky, your task is to go above or below depending on the position of the wall. Refer fig. 2 for the two possible cases that you will encounter.


<div class="fig fighighlight">
  <img src="/assets/2019/p4/wall.png" width="80%">
  <div class="figcaption">
    Figure 1: Task 2 - Two possible scenerios for the wall placements.
  </div>
  <div style="clear:both;"></div>
</div>

Note that you cannot go left or right of the metal bars. You are restricted to a height of 2.5 meters for this project. If you fly above 2.5m, your task will be counted as unsuccessful. Also, the wall is equiped with a lot of visual features so you can detect it easily.

You can collect data as a ROS bag/video from the downfacing and frontfacing cameras of the river-bridge scene and the wall in IRB lab 0108. Feel free to change the illumination of the room. Define the coordinates as $$(0, 0, 0)$$ as the starting pose (the first frame).

<a name='implementation'></a>
## 3. Implementation
This project it totally open! You can use any open-source code available online to solve any part of the problem. Make sure you cite them. You can also learn the textures on the floor to distinguish between the river and the bridge. A sample texture is available in the lab. 

For estimating the depth (and relative pose) of the wall from front facing camera in absolute scale, you need odometry estimates from the bottom facing camera. Using `Kalibr`, calibrate the bottom facing camera with IMU; calibrate front facing camera with IMU and get the relative transformation (Rotation and Translation or extrinsics) between front facing camera and bottom facing camera. Now, both cameras are running a version odometry estimation. Use the extrinsic calibration to provide a metric scale for the front facing camera. Make sure your data is time syncronized before running through the `Kalibr`. You can use `TimeSynchronizer` for that. [Link](http://wiki.ros.org/message_filters#Time_Synchronizer)
For the bottom facing camera depth estimation, you can use your results from Project 4a or any online open-source code.
**YOU CAN ALSO USE THE HEIGHT MEASUREMENT OF THE SONAR!**

<a name='rosnodes'></a>
### 3.1. ROS Nodes
You need to create one or multiple ROS node(s) to run your algorithm for each task. You have to publish trajectory for both tasks as `nav_msgs/Odometry` (accumulated instantaneous camera pose).

<a name='launch'></a>
### 3.2. Launch File
All the above ROS node(s) must be called using a single `launch` file.

<a name='rviz'></a>
### 3.3. Rviz visualization
You are required to plot your estimated 3D camera pose in `rviz` along with the odometry (`nav_msgs/Odometry`) from the PRG Husky using rviz tf like you did in the previous projects.

<a name='sub'></a>
## 4. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit. </b>

<a name='report'></a>
### 4.1. Report

Explain in detail your approach to complete the project, and describe any interesting problems you encountered and/or solutions you implemented.  You **MUST** include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder (Use the same draft folder from P1) and should of a conference quality paper.
- Present the output videos for your estimated trajectory (for both cases: Helix and straight line) following along with the odometry output from PRG Husky, stereo (both left and right) frames as ``Outputs/StereoVO.mp4``.

<a name='files'></a>
### 4.2. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``TeamYourTeamNumber_p4a.zip``. If you email ID is ``1``, then the submission file should be named ``Team1_p4a.zip``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission `zip` file.

```
TeamYourTeamNumber_p4a.zip
│   README.md
|   Your Code files 
|   ├── Any subfolders you want along with files 
|   Outputs
|   ├── StereoVO.mp4
|   └── StereoVO-Features.mp4
└── Report.pdf
```

<a name='debug'></a>
## 5. Debugging Tips
- To verify if your detections are working correctly, you can re-project the features using the estimated pose onto the next frame (they should be close to the tracked features).

<a name='allowed'></a>
## 6. Allowed and Disallowed functions

<b> Allowed:

Any functions regarding reading, writing and displaying/plotting images and windows in `cv2`, `matplotlib`, `ROS`.
- Basic math utilities including convolution operations in `numpy` and `math`.
- Any functions for pretty plots.
- ``bebop_autonomy`` packages for controlling the PRGHusky.
- Any function that computes features/corners.
- Any function that matches feature correspondences.
- Any function that performs KLT or any other feature tracker.

<b> Disallowed:
- Any function that computes sparse or dense optical flow.
- Any function that computes RANSAC. Although, you can use any least square solver.

<a name='hw'></a>
## 7. Hardware Tips

<a name='duo'></a>
### 7.1. Duo3D Camera Driver
Follow the steps from [this repo](https://github.com/NitinJSanket/Duo3D-Setup) to install the Duo3D camera driver.

<a name='calibration'></a>
### 7.2. Camera Calibration
The Duo3D camera comes calibrated out of the factory and gives only the calibrated images. You can also use the [Kalibr](https://github.com/ethz-asl/kalibr/wiki/camera-imu-calibration) package from ETH-Z to re-calibrate the duo cameras if needed.

<a name='coll'></a>
## 8. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own team's, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the ENAE788M Fall 2019 website.
