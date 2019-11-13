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

Your PRG Husky platform is equipped with a front facing RGB camera, a down facing stereo grayscale and an IMU. For the first task, you are in a space with a thin river-like band of blue sheet. Only a small region has a ladder

compute the 3D camera trajectory of a stereo sensor. Imagine your stereo sensor (DUO Camera) is on a quadrotor facing downwards. You can assume that the ground that the camera sees is <b>planar</b>. You need to collect data as a ROS bag/video flying the PRG Husky platform. You can use the carpets in lab IRB 0108. Feel free to change the illumination of the room. Define the coordinates as $$(0, 0, 0)$$ as the starting pose (the first frame). 

<a name='implementation'></a>
## 3. Implementation
You need to run the Helix trajectory from [Project 2](https://prgaero.github.io/2019/proj/p2/) and a straight line trajectory (from $$[0,0,0]m$$ to $$[2,2,2]m$$; and record a ROS Bag. The entire class can have the common data if you want. Team BRZ had the best trajectory following in Project 2. Work with team BRZ to get the data. Make sure your stereo calibration is correct. You need to record both camera data (and IMU if you want to). If you experience frame drops while bagging, reduce the frame rate using ROS `throttle` DUO-Camera SDK gives both raw IMU values as well as filtered attitude. Feel free to use it if you want.

From one of the camera, say the left camera for an instance, you will be detecting features in the 'current frame'. You can use Harris, SIFT, FAST, SURF or any other feature detector. You can use any open source code for feature detection. For all the corners in the image, you will then compute the sparse optical flow between two consecutive frames using Kanade-Lucas-Tomasi Tracker (KLT). Feel free to use any open source code for KLT or any other feature tracker. If you are feeling extra enthusiastic, you can implement a tracker on your own. In your ROS bag, you will get the image frames along with the ROS timestamps. Using timestamps and sparse optical flow, you will get the $$[\dot{x}, \dot{y}]^T$$ in the calibrated image coordinates. Although, these timestamps are **NOT** perfect and may have high frequency noise. Assuming that the images are taken at a constant rate, you can simply use a low-pass filter on the $$\Delta t$$ to get better results. You can do `rostopic hz` to get the publish rate.

Now, given a corner in the calibrated image coordinates $$[x,y]^T$$ and its corresponding optical flow $$[\dot{x},\dot{y}]^T$$, you can solve for the linear and angular velocities of the camera:


$$
\begin{bmatrix}
\dot{x} \\
\dot{y}
\end{bmatrix} = 

\begin{bmatrix}
\mathbf{f_1}(x,y,Z)\\
\mathbf{f_2}(x,y,Z)
\end{bmatrix}

\begin{bmatrix}
V_x \\
V_y \\
V_z \\
\Omega_x \\
\Omega_y \\
\Omega_z \\
\end{bmatrix} $$

where $$[V_x, V_y, V_z, \Omega_x, \Omega_y, \Omega_z]^T$$ are the linear and angular velocities to be estimated. The functions $$\mathbf{f_1(\cdot)}$$, $$\mathbf{f_2(\cdot)}$$ are $$1\times 6$$ vectors. The above equation is nothing but the optical flow equation in a much more compressed form. $$Z$$ is the depth of the corner/pixel. You can estimate $$Z$$ or 'camera-$$Z$$' using the stereo pair by feature matching. Again, you are allowed to use any off-the-shelf feature matching algorithm but you need to compute $$Z$$ from the matched features on your own. Note that this is the camera $$Z$$ which may or may not be equal to the height of the quadrotor due to non-zero roll and pitch angle.
**YOU ARE NOT ALLOWED TO USE THE HEIGHT MEASUREMENT OF THE SONAR!**

#### RANSAC

Optical flow computation are prone to outliers and you will need to reject them using RANSAC. Three sets of constraints are required to solve the above linear equation and thus you can perform a 3-point RANSAC for outlier rejection.

You should now get a good estimate of linear and angular velocities which can be integrated (using $$\Delta t$$ ROS timestamps) to compute position and orientation.


<a name='rosnodes'></a>
### 3.1. ROS Nodes
You need to create one or multiple ROS node(s) to run your algorithm for pose estimation. You have to publish instantaneous velocities as `geometry_msgs/Twist` and trajectory as `nav_msgs/Odometry` (accumulated instantaneous camera pose).

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
- Present the output videos for your estimated trajectory (for both cases: Helix and straight line) in `rviz` along with the detected features in the world frame as ``Output/StereoVO-Features.mp4``.

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
