---
layout: page
mathjax: true
title: The Final Race!
permalink: /2019/proj/p5/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
  - [2.1. Stage 1: Wall](#wall)
  - [2.2. Stage 2: Window](#window)
  - [2.3. Stage 3: Bridge](#bridge)
  - [2.4. Stage 4: Circular Bullseye](#circbullseye)
  - [2.5. Stage 5: Wall Again!](#wallagain)
  - [2.6. Stage 6: Finish Tag](#finishtag)
- [3. Attempt Termination](#terminate)
- [4. Scoring Criterion](#score)
- [5. D-Day of the Competition](#dday)
- [3. Implementation](#implementation)
	- [3.1. ROS Nodes](#rosnodes)
	- [3.2. Launch File](#launch)
	- [3.3. Rviz visualization](#rviz)
	- [3.4. Camera Calibration](#calib)
- [4. Submission Guidelines](#sub)
  - [4.1. Report](#report)
  - [4.2. File tree and naming](#files)
- [5. Debugging Tips](#debug)
- [6. Allowed and Disallowed functions](#allowed)
- [7. Live Demo](#demo)
- [8. Hardware Tips](#hw)
	- [8.1. Duo3D Camera Driver](#duo)
	- [8.2. Camera Calibration](#calibration)
- [9. Collaboration Policy](#coll)

<a name='due'></a>
## 1. Deadline 
**11:59PM, Monday, December 16, 2019** for report submission.

<a name='intro'></a>
## 2. Problem Statement
Congratulations for making this far into the course. We know that you've worked very hard to get here and learnt a lot of new concepts along the way. Now, it's time to put everything together. The aim of this project is to win the race on an obstacle course which utilizes all the algorithms you built before from projects 1 through 4. 


Remember that your PRGHusky comes with a suite of sensors, a front facing RGB color global shutter camera, a down facing stereo gryscale camera with an IMU along with the SONAR on-board and odometry estimates from the ``bebop_autonomy`` package. You can use any/all of the sensors to complete the course as quickly as you can. Also, the structure of the track (obstacle course) is known before along with a prior on pose of the obstacles as a gaussian distribution. An overview of the track is shown in Fig. 1. 

<div class="fig fighighlight">
  <img src="/assets/2019/p5/Track.png" width="60%">
  <div class="figcaption">
    Figure 1: Overview of the track.
  </div>
  <div style="clear:both;"></div>
</div>

The track contains exactly **six** stages.  Description of each stage is given next.

<a name='wall'></a>
### 2.1. Wall

In the first stage, you take off from the helipad and you have to navigate though a wall on the floor, i.e., you have to fly over it. Note that the wall has features on it to help depth estimation. This is the same wall we used in [project 4b](/2019/proj/p4b/). The sample photo of the wall is given in Fig. 2.

<div class="fig fighighlight">
  <img src="/assets/2019/p4/wall-real.jpg" width="60%">
  <div class="figcaption">
    Figure 2: Stage 1: Wall on the ground.
  </div>
  <div style="clear:both;"></div>
</div>



<a name='window'></a>
### 2.2. Window

In the second stage, you have to traverse through a yellow window, this is the same window we used in [project 3a](/2019/proj/p3a/). A sample photo of the window is given in Fig. 3. Remember that the window looks different due to changes in lighting. Here, the size, shape and height of the window are known. But the pose is only known as a gaussian distribution.

<div class="fig fighighlight">
  <img src="/assets/2019/p5/YellowWindow.png" width="60%">
  <div class="figcaption">
    Figure 3: Stage 2: Window.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='bridge'></a>
### 2.3. Bridge

In the third stage, you have to fly over the bridge (atleast half of the PRGHusky has to be over the bridge to count as a success), this is the same bridge we used in [project 4b](/2019/proj/p4b/). A sample photo of the bridge over the river is given in Fig. 4.

<div class="fig fighighlight">
  <img src="/assets/2019/p4/river-ladder-real.jpg" width="60%">
  <div class="figcaption">
    Figure 4: Stage 3: Bridge over the river.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='circbullseye'></a>
### 2.4. Circular Bullseye

In the fourth stage, you have to land over a circular bullseye, this is the same bullseye target we used in [project 3b](/2019/proj/p3b/). A sample photo of the circular bullseye is given in Fig. 5. As before, please print out your own bullsye tags for testing from [here](/assets/2019/p3/CircularTag.png). Also, remember that the bullseye tag is reflective.

<div class="fig fighighlight">
  <img src="/assets/2019/p3/CircularTag2.png" width="60%">
  <div class="figcaption">
    Figure 5: Stage 4: Circular Bullseye from different views.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='wallagain'></a>
### 2.5. Wall Again!

In the penultimate stage, you take off from the circular bullseye and navigate through a wall again. This time the wall is up in the air, i.e., you have to fly below it. Note that the wall has features on it to help depth estimation. This is a wall similar to the one we used in [project 4b](/2019/proj/p4b/).

- Add photo here

<a name='finishtag'></a>
### 2.6. Finish Tag

For the finish line, you have to land on a square tag. please print out your own square tags for testing from [here](/assets/2019/p5/SquareTag.png). Also, remember that the square tag is reflective. 

- Add photo here

Congrats on finishing the course! Wohoooooo!


<a name='terminate'></a>
## 3. Attempt Termination
Doing any of these will instantly terminate your attempt. 
- Crossing the river at any time which is not over the bridge.
- Flying over a height of 2.5 m. 
- Failing to navigate in any of the previous stages before proceeding to the next one.
- Crashing into any of the obstacles/track objects and/or the nets.
- Landing due to battery failsafe.
- Going over the maximum time of 2 mins per attempt.

<a name='score'></a>
## 4. Scoring Criterion
Taking off from the helipad gives the team 10 points and then crossing each stage of track will get the team 15 points, totalling a maxmimum of 100 points for each attempt. The team's attempt will be terminated in any of the mentioned things in [Section 3](#terminate) happen. If the number of stages between two teams are tied, then the team with the lower time comes out on top. 

<a name='dday'></a>
## 5. D-Day of the Competition
On the day of the competition, the teams will go in the order of their team number. Each team will get a maximum of five attempts and a maximum time of 2 minutes per attempt and a maximum time of 15 minutes for all five attempts. Between attempts, the team can use any amount of time (within the alloted 15 minutes of maximum time) to fix any software/hardware bugs or do changes in hardware/software (including change of batteries).

The team with the highest points will win. Note that, completing the course (within the 2 minute slot per attempt) will get that team the maximum of 100 points.  



<a name='implementation'></a>
## 6. Implementation
This project it totally open! You can use any open-source code available online to solve any part of the problem. Make sure you cite them. You can also learn the textures on the floor to distinguish between the river and the bridge. A sample texture is available in the lab. 

For estimating the metric depth (and relative pose) of the wall from front facing camera in absolute scale, you need odometry estimates from the bottom facing camera. Using `Kalibr`, calibrate the bottom facing camera with IMU; calibrate front facing camera with IMU and get the relative transformation (Rotation and Translation or extrinsics) between front facing camera and bottom facing camera. Now, both cameras are running a version odometry estimation. Use the extrinsic calibration to provide a metric scale for the front facing camera. Make sure your data is time syncronized before running through the `Kalibr`. You can use [`TimeSynchronizer`](http://wiki.ros.org/message_filters#Time_Synchronizer) for this.
For the bottom facing camera depth estimation, you can use your results from Project 4a or any online open-source code.
**YOU CAN ALSO USE THE HEIGHT MEASUREMENT OF THE SONAR AND ODOMETRY FROM `bebop_autonomy`!**

<a name='rosnodes'></a>
### 6.1. ROS Nodes
You need to create one or multiple ROS node(s) to run your algorithm for each task. You have to publish trajectory for both tasks as `nav_msgs/Odometry` (accumulated instantaneous camera pose).

<a name='launch'></a>
### 6.2. Launch File
All the above ROS node(s) must be called using a single `launch` file.

<a name='rviz'></a>
### 6.3. Rviz visualization
You are required to plot your estimated 3D camera pose in `rviz` along with the odometry (`nav_msgs/Odometry`) from the PRG Husky using rviz tf like you did in the previous projects.
For Task 2, you need to plot the wall in rviz along with the trajectory (and pose i.e. both position and orientation) of your quadrotor.  This visualization is similar to what you did in Project 3b (Mini Drone Race). Be sure to fix your wall in some arbitrarily chosen world frame and plot your camera’s (quadrotor’s) pose with respect to it.

<a name='calib'></a>
### 6.4 Camera Calibration

Camera Intrinsic and Extrinsic calibration entails with estimating the camera calibration matrix K which includes the focal length and the principal point and the distortion parameters and relative rotation and translation ($$R$$ and $$T$$) between a set of sensors. You’ll need to use the awesome calibration package developed by ETHZ Kalibr to do this. You’ll need either a checkerboard or an april grid to calibrate the camera. We found that using the April grid gave us superior results. Feel free to print one (don’t forget to turn off autoscaling or scaling of any sort before printing). Bigger april grids or checkerboard in general give more accurate results. A large april grid is located in IRB 3237 (Fig. 4) which you are free to use if you don’t want to print your own.

<a name='sub'></a>
## 7. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit. </b>

<a name='report'></a>
### 7.1. Report

Explain in detail your approach to complete the project, and describe any interesting problems you encountered and/or solutions you implemented.  You **MUST** include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder (Use the same draft folder from P1) and should of a conference quality paper.
- Present the output videos for your estimated trajectory while going above the bridge and stereo (both left and right) frames as ``Outputs/Task1.mp4``.
- Present the output videos for trajectory following along with the wall detection overlaid on the video, rviz visualization of 3D wall pose estimates in real-time as ``Outputs/Task2.mp4`` for Task 2.

<a name='files'></a>
### 7.2. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``TeamYourTeamNumber_p4b.zip``. If you email ID is ``1``, then the submission file should be named ``Team1_p4b.zip``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission `zip` file.

```
TeamYourTeamNumber_p4a.zip
│   README.md
|   Your Code files 
|   ├── Any subfolders you want along with files 
|   Outputs
|   ├── Task1.mp4
|   └── Task2.mp4
└── Report.pdf
```

<a name='debug'></a>
## 5. Debugging Tips
- To verify if your extrinsic calibration is correct, measure the translation between the sensors using a standard ruler. If it is far from calibrated translation, you definitely have done something wrong with your calibration. 

<a name='allowed'></a>
## 6. Allowed and Disallowed functions

<b> Allowed:</b>

Any functions regarding reading, writing and displaying/plotting images and windows in `cv2`, `matplotlib`, `ROS`.
- Basic math utilities including convolution operations in `numpy` and `math`.
- Any functions for pretty plots.
- ``bebop_autonomy`` packages for controlling the PRGHusky.
- Any function that computes features/corners.
- Any function that matches feature correspondences.
- Any function that performs KLT or any other feature tracker.
- Any function that computes sparse or dense optical flow.
- Any function that computes RANSAC. Although, you can use any least square solver.
- Any function that fits a plane.
- Any function that solves entire structure from motion.

<b> Disallowed:</b>
- NOTHING!

<a name='demo'></a>
## 7. Live Demo

On the day of the deadline, each team will be given a 15 minute slot for demonstrating their code in action to the instructors. 
For Task 2, the instructors will place the quadrotor such that the river-bridge scene is in the front facing camera $$Z$$ direction (or infront of the PRG Husky). Note that you will NOT be able to see the bridge from the front facing camera once you take-off from ground. You need to go above the bridge to solve Task 2. If more than 50% of the PRG Husky volume is above the bridge, it will be counted as success. 

For Task 1, the instructors will place the wall (at arbitrary height) as well as the PRG Husky quadrotor as they wish (position, orientation). The instructors will make sure that atleast a major part of the wall is in the visible region as seen from the first frame (note that it is not guarenteed that the complete window will be visible in the first frame). The task is the fly above or below the window as fast as possible. You also need to show us a live visualization of your detection (corners of the window overlaid on the image) along with the 3D visualization of the window with the relative camera pose overlaid in rviz. If you don't go between the two metal bars, or go above `2.5m` in altitude, it will be counted as a failure.

You can have ANY number of trials in 15 mins for both combined. Only the best trial will be graded.<br>
**THE ENTIRE AREA WILL HAVE FEATURES (CARPETS)!!**

**LIVE DEMO TIMINGS WILL BE RELEASED LATER.**

<a name='hw'></a>
## 8. Hardware Tips

<a name='duo'></a>
### 8.1. Duo3D Camera Driver
Follow the steps from [this repo](https://github.com/NitinJSanket/Duo3D-Setup) to install the Duo3D camera driver.

<a name='calibration'></a>
### 8.2. Camera Calibration
The Duo3D camera comes calibrated out of the factory and gives only the calibrated images. You can also use the [Kalibr](https://github.com/ethz-asl/kalibr/wiki/camera-imu-calibration) package from ETH-Z to re-calibrate the duo cameras if needed.

<a name='coll'></a>
## 9. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own team's, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the ENAE788M Fall 2019 website.
