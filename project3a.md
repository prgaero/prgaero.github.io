---
layout: page
mathjax: true
title: GapFlyt
permalink: /2019/proj/p3a/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
- [3. Testing](#test)
- [4. Submission Guidelines](#sub)
  - [4.1. Report](#report)
  - [4.2. File tree and naming](#files)
- [5. Allowed and Disallowed functions](#allowed)
- [6. Collaboration Policy](#coll)

<a name='due'></a>
## 1. Deadline 
**11:59PM, Thursday, October 17, 2019** for submission of the report and video.

<a name='intro'></a>
## 2. Problem Statement
In this project, your aim is to navigate through colored window sequence of known sizes but unknown position and orientation. The windows are setup in the lab IRB 0108. You need to collect data as a ROS bag/video capture while moving the camera pointed at different angles (possible different illumination) of the window. Feel free to place the windows at any distance and orientation you desire for your testing. You'll need to implement the detection algorithm of windows using color or edges or whatever you desire.  

<a name='test'></a>
## 3. Testing
On the day of the deadline, each team will be given a 15 minute slot for demoing their code in action to the instructors. The instructors will place the windows as they wish (position, orientation and order of color). The task is the fly through the windows as fast as possible.  


<a name='sub'></a>
## 4. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit </b>

<a name='report'></a>
### 4.1. Report

Explain in detail your approach to complete the project, and describe any interesting problems you encountered and/or solutions you implemented.  You **MUST** include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder (Use the same draft folder from P1) and should of a conference quality paper.
- Present Vicon plots for each trajectory followed along with the estimated 3D window position overlaid on the same plot. (Show all three views ``X-Y``, ``X-Z`` and ``Y-Z``).
- Present the output videos for trajectory following along with the window estimates in real-time as ``Outputs/GapFlyt.mp4``. Be sure to use appropriate colors to plot the windows in ``rviz``, for eg., blue color for a blue window and so on.


<a name='files'></a>
### 4.2. File tree and naming

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


<a name='allowed'></a>
## 5. Allowed and Disallowed functions

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
## 6. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own team's, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the ENAE788M Fall 2019 website.
