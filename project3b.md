---
layout: page
mathjax: true
title: Circular Bullseye
permalink: /2019/proj/p3b/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
- [3. Testing](#test)
- [4. Submission Guidelines](#sub)
  - [4.1. Report](#report)
  - [4.2. File tree and naming](#files)
- [5. Debugging Tips](#debug)
- [5. Allowed and Disallowed functions](#allowed)
- [6. Collaboration Policy](#coll)

<a name='due'></a>
## 1. Deadline 
**11:59PM, Tuesday, October 29, 2019** for submission of the report and video.

<a name='intro'></a>
## 2. Problem Statement
In this project, your aim is to find a circular bullseye and land on it. You are given the approximate co-ordinates (as a Gaussian distribution) of the bullseye from your starting point. The circular bullseye is setup in the lab IRB 0108. You need to collect data as a ROS bag/video capture while moving the monocular + stereo camera is pointed at different angles (possible different illumination) of the circular bullseye.

<div class="fig fighighlight">
  <img src="/assets/2019/p3/CircularBullseye.png" width="80%">
  <div class="figcaption">
    Figure 1: (a) Circular bullseye target, (b) Sample landing on circular bullseye.
  </div>
  <div style="clear:both;"></div>
</div>

<a name='test'></a>
## 3. Testing
On the day of the deadline, each team will be given a 15 minute slot for demoing their code in action to the instructors. The instructors will place the circular bullseye as they wish (position with gaussian given). The task is to land on the circular target. 
Specifically, the team will place their PRG Husky at the corner of the flying space and then the instructors will place the circular bull's eye tag at \((X,Y)\) relative to the PRG Husky initial position with a covariance \((\Sigma_x, Sigma_y)\). Your task is to take off, adjust your position according to the position of tag and then land on the tag.

<a name='sub'></a>
## 4. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit </b>

<a name='report'></a>
### 4.1. Report

Explain in detail your approach to complete the project, and describe any interesting problems you encountered and/or solutions you implemented.  You **MUST** include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder (Use the same draft folder from P1) and should of a conference quality paper.
- Present Vicon plots for each trajectory followed along with the estimated 3D bullseye center position overlaid on the same plot. (Show all three views ``X-Y``, ``X-Z`` and ``Y-Z``).
- Present the output videos for trajectory following along with the 3D bullseye center position estimates in real-time as ``Outputs/Bullseye.mp4``.


<a name='files'></a>
### 4.2. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``TeamYourTeamNumber_p3b.zip``. If you email ID is ``1``, then the submission file should be named ``Team1_p3b.zip``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission.

```
TeamYourTeamNumber_p3a.zip
│   README.md
|   Your Code files 
|   ├── Any subfolders you want along with files 
|   Outputs
|   └──  Bullseye.mp4
└── Report.pdf
```

<a name='debug'></a>
## 5. Debugging Tips
- To verify if your detections are working correctly, plot the corners of the window on the image, they should align with the true window corners. 
- To verify if your pose estimation is correct, re-project the estimated 3D corners of the window onto the image. They should be very close to the detected corners.

<a name='allowed'></a>
## 5. Allowed and Disallowed functions

<b> Allowed:

Any functions regarding reading, writing and displaying/plotting images and windows in `cv2`, `matplotlib`, `ROS`.
- Basic math utilities including convolution operations in `numpy` and `math`.
- Any functions for pretty plots.
- ``bebop_autonomy`` packages for controlling the PRGHusky.

<b> Disallowed:
- Any function that implements trajectory interpolation.
- Any function that directly detects the window.
- Functions for contour fitting.


<a name='coll'></a>
## 6. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own team's, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the ENAE788M Fall 2019 website.
