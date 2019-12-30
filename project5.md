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
- [6. Implementation](#implementation)
	- [6.1. ROS Nodes](#rosnodes)
	- [6.2. Launch File](#launch)
	- [6.3. Service Call](#service)
	- [6.4. Image Resolution](#img-res)
  - [6.5. Code Speedup](#codespeedup)
- [7. Submission Guidelines](#sub)
  - [7.1. Report](#report)
  - [7.2. File tree and naming](#files)
- [8. Allowed and Disallowed functions](#allowed)
- [9. Grading](#grading)
- [10. Collaboration Policy](#coll)

<a name='due'></a>
## 1. Deadline 
**11:59PM, Monday, December 16, 2019** for report and video submission. 

**YOU ARE NOT ALLOWED TO USE ANY LATE DAYS FOR THIS PROJECT!**

<a name='intro'></a>
## 2. Problem Statement
Congratulations for making this far into the course. We know that you've worked very hard to get here and learnt a lot of new concepts along the way. Now, it's time to put everything together. The aim of this project is to win the race on an obstacle course which utilizes all the algorithms you built from projects 1 through 4. 


Remember that your PRGHusky comes with a suite of sensors, a front facing RGB color global shutter camera, a down facing stereo grayscale camera with an IMU along with the SONAR on-board and odometry estimates from the ``bebop_autonomy`` package. You can use any/all of the sensors to complete the course as quickly as you can. Also, the structure of the track (obstacle course) is known before along with a prior on pose of the obstacles as a gaussian distribution. An overview of the track is shown in Fig. 1. 

<div class="fig fighighlight">
  <img src="/assets/2019/p5/Track.png" width="100%">
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

In the second stage, you have to traverse through a yellow window, this is the same window we used in [project 3a](/2019/proj/p3a/). A sample photo of the window is given in Fig. 3. Remember that the window looks different from different viewpoints and changes in lighting. Here, the size, shape and height of the window are known. But the pose is only known as a gaussian distribution.

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
  <img src="/assets/2019/p5/RiverBridge.jpeg" width="100%">
  <div class="figcaption">
    Figure 4: Stage 3: Bridge over the river.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='circbullseye'></a>
### 2.4. Circular Bullseye

In the fourth stage, you have to land over a circular bullseye, this is the same bullseye target we used in [project 3b](/2019/proj/p3b/). A sample photo of the circular bullseye is given in Fig. 5. As before, please print out your own bullsye tags for testing from [here](/assets/2019/p3/CircularTag.png). Also, remember that the bullseye tag is reflective.

<div class="fig fighighlight">
  <img src="/assets/2019/p3/CircularTag2.png" width="100%">
  <div class="figcaption">
    Figure 5: Stage 4: Circular Bullseye from different views.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='wallagain'></a>
### 2.5. Wall Again!

In the penultimate stage, you take off from the circular bullseye and navigate through a wall again. This time the wall is up in the air, i.e., you have to fly below it. Note that the wall has features on it to help depth estimation. This is a wall similar to the one we used in [project 4b](/2019/proj/p4b/).

<div class="fig fighighlight">
  <img src="/assets/2019/p5/WallUp.jpg" width="60%">
   <div class="figcaption">
    Figure 6: Stage 2: Wall on the top.
   </div>
<div style="clear:both;"></div>
</div>

<a name='finishtag'></a>
### 2.6. Finish Tag

For the finish line, you have to land on a square tag. please print out your own square tags for testing from [here](/assets/2019/p5/SquareTag.png). Also, remember that the square tag is reflective. 


<div class="fig fighighlight">
  <img src="/assets/2019/p5/SquareTagReal.jpeg" width="60%">
   <div class="figcaption">
    Figure 6: Stage 6: Square Tag.
   </div>
<div style="clear:both;"></div>
</div>


Congrats on finishing the course! Wohoooooo!


<a name='terminate'></a>
## 3. Attempt Termination
Doing any of the following will instantly terminate your attempt: 
- Crossing the river at any time which is not over the bridge.
- Flying over a height of 2.5 m. 
- Failing to navigate in any of the previous stages before proceeding to the next one.
- Crashing into any of the obstacles/track objects and/or the nets.
- Landing due to battery failsafe.
- Going over the maximum time of 2 mins per attempt.

<a name='score'></a>
## 4. Scoring Criterion
Taking off from the helipad gives the team 10 points and then crossing each stage of track will get the team 15 points, totalling a maxmimum of 100 points for each attempt. The team's attempt will be terminated if any of the things mentioned in [Section 3](#terminate) happen. If the number of stages between two teams are tied, then the team with the lower time comes out on top. 

<a name='dday'></a>
## 5. D-Day of the Competition
On the day of the competition, the teams will go in the order of their team number. Each team will have a maximum time of 2 minutes per attempt and a maximum time of 15 minutes for all attempts combined. Between attempts, the team can use any amount of time (within the alloted 15 minutes of maximum time) to fix any software/hardware bugs or do changes in hardware/software (including change of batteries). Only the best trial will be graded.

A sample photo of the real track is shown in Fig. 7.


<div class="fig fighighlight">
  <img src="/assets/2019/p5/TrackPhoto.jpg" width="100%">
   <div class="figcaption">
    Figure 7: The Real Track.
   </div>
<div style="clear:both;"></div>
</div>


Exactly 2 hours before the demo, each team can go and measure the distances in the track. No one will be allowed to enter the track 1 hour before the demo. The instructors will displace each obstacle randomly with a maximum disturbance of 60 cm in both X and Y directions (Z pointing up) and maximum orientation displacement of +/- 10 degrees. 

The team with the highest points will win. Note that, completing the course (within the 2 minute slot per attempt) will get that team the maximum of 100 points.  

The teams can place the quadrotor on the helipad in any desired orientation. Also, if a team wants to improve their live-demo score, they can request for an additional slot after all the teams have finished their demo with a penalty of 20 points of the total project 5 grade. 


<a name='implementation'></a>
## 6. Implementation
This project is totally open! You can use any open-source code available online to solve any part of the problem. Make sure you CITE them. You are expected to use the implementations from the previous four projects but are NOT limited to it. **You are NOT allowed to modify the PRGHusky platform.** This includes adding/subtracting any sensors. Your results are ONLY limited by your imagination and creativity!

<a name='rosnodes'></a>
### 6.1. ROS Nodes
You need to create one or multiple ROS node(s) to run your algorithm for each task. You have to publish trajectory for the entire task as `nav_msgs/Odometry` (accumulated instantaneous camera pose).

<a name='launch'></a>
### 6.2. Launch File
All the above ROS node(s) must be called using a single `launch` file.

<a name='service'></a>
### 6.3. Service Calls
Running a lot of nodes might be heavy for the Up board to handle. `Service Calls` in `ROS` are recommended.

<a name='img-res'></a>
### 6.4. Image Resolution
Depending on your algorithm, you would want to drop down the resolution of the image to make algorithm faster. Note that resizing the images will change the intrinsic calibration $$K$$ matrix.

<a name='codespeedup'></a>
### 6.5. Code Speedup
Wherever possible, try to use C++ or ``numpy`` functions to speed-up your computations. 

<a name='sub'></a>
## 7. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit. </b>

<a name='report'></a>
### 7.1. Report

Explain in detail your approach to complete the project, and describe any interesting problems you encountered and/or solutions you implemented.  You **MUST** include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder (Use the same draft folder from P1) and should of a conference quality paper.
- You need to submit an `mp4` presentation video (atleast 1080p resolution and a maximum of 15 mins, preferably with the presenter's face and slides) and presentation `pdf` file explaining your algorithm, implmentation-level details, how you overcame them and future scope. This is due at 11:59:59 pm on Dec 16, 2019.

<a name='files'></a>
### 7.2. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``TeamYourTeamNumber_p5.zip``. If you email ID is ``1``, then the submission file should be named ``Team1_p5.zip``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission `zip` file.

```
TeamYourTeamNumber_p5.zip
│   README.md
|   Your Code files 
|   ├── Any subfolders you want along with files 
|   Presentation.mp4
└── Report.pdf
```

<a name='allowed'></a>
## 8. Allowed and Disallowed functions

<b> Allowed:</b>
- **ANYTHING IN THE WORLD!**

<b> Disallowed:</b>
- **ABSOLUTELY NOTHING!**

<a name='grading'></a>
## 9. Grading
The final grade for this project will be computed as follows: 70% of the grade is calculated from the live demo/performance on D-Day, 15% of the grade is given for the Report and the remaining 15% of the grade is awarded for the Presenation video.

<a name='coll'></a>
## 10. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own team's, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the ENAE788M Fall 2019 website.
