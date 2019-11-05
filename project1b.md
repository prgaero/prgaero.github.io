---
layout: page
mathjax: true
title: Non-stinky Unscented Kalman Filter for Attitude Estimation
permalink: /2019/proj/p1b/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
- [3. Implementation](#implementation)
- [4. Submission Guidelines](#sub)
  - [4.1. File tree and naming](#files)
  - [4.2. Report](#report)
- [5. Allowed and Disallowed functions](#funcs)
- [6. Collaboration Policy](#coll)
- [7. Acknowledgements](#ack)

<a name='due'></a>
## 1. Deadline 
**11:59 PM, September 24, 2019.**

<a name='prob'></a>
## 2. Problem Statement 
In this project, you will implement an Unscented Kalman Filter (UKF) to track three dimensional orientation. Given IMU sensor readings from gyroscopes and accelerometers, you will estimate the underlying 3D orientation and compare it with the ground truth data given by a Vicon motion capture system. 

Follow the steps 3 to 4 from [Project 1a](https://prgaero.github.io/2019/proj/p1a/) for instructions on reading the data and sensor calibration.


<a name='implementation'></a>
## 3. Implementation
You estimated the orientation using a Madgick Filter in Project 1a, now it's time to implement a non-linear filter - UKF. Follow [this paper](https://ieeexplore.ieee.org/document/1257247) by Edgar Kraft for more details.  You can compare your resulting orientation estimate with the “ground truth” estimate from the Vicon. A simple plotting function is provided in “rotplot.py.” This function provides basic visualization and can be modified as you see fit. 
Make sure you plot the orientation in all axis and compare with Vicon plots.

<a name='testset'></a>
## 4. Notes About Test Set
A test set will be released 24 hours before the deadline. You can download the test set from <b>here</b>. Your report MUST include the output from both the train and test sets. 


<a name='sub'></a>

## 5. Submission Guidelines

**If your submission does not comply with the following guidelines, you'll be given ZERO credit.**

### 5.1. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``YourDirectoryID_p1b.zip``. If you email ID is ``abc@umd.edu`` or ``abc@terpmail.umd.edu``, then your ``DirectoryID`` is ``abc``. For our example, the submission file should be named ``abc_p1b.zip``. The file **must have the following directory structure**. The file to run for your project should be called ``YourDirectoryID_p1b/Code/Wrapper.py``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. 

<p style="background-color:#ddd; padding:5px">
<b>NOTE:</b> 
Please <b>DO NOT</b> include data in your submission. Furthermore, the size of your submission file should <b>NOT</b> exceed more than <b>20MB</b>.
</p>

The file tree of your submission <b>SHOULD</b> resemble this:

```
YourDirectoryID_p1b.zip
├── Code
|   ├── Wrapper.py
|   └── Any subfolders you want along with files
├── Report.pdf
└── README.md
```

<a name='report'></a>

### 5.2. Report

For each section of the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented. You must include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder and should of a conference quality paper. Feel free to use any online tool to edit such as [Overleaf](https://www.overleaf.com) or install LaTeX on your local machine.
- Link to the `rotplot` videos comparing attitude estimation using Madgwick Filter from Project 1a, UKF and Vicon. Sample video can be seen [here](https://www.youtube.com/watch?feature=player_embedded&v=iCe3o-9moUM).
- Plots for all the train and test sets. In each plot have the angles estimated from madgwick filter, UKF and Vicon along with proper legend.  
- A sample report for a similar project is given in the `.zip` file given to you with the name `SampleReport.pdf`. Treat this report as the benchmark or gold standard which we'll compare your reports to for grading.


<a name='funcs'></a>

## 6. Allowed and Disallowed functions

<b> Allowed:</b>

- Any functions regarding reading, writing and displaying/plotting images in `cv2`, `matplotlib`
- Basic math utitlies including convolution operations in `numpy` and `math`
- Any functions for pretty plots
- Quaternion libraries
- Any library that perform tranformation between various representations of attitude

<b> Disallowed:</b>

- Any function that implements in-part or full UKF

If you have any doubts regarding allowed and disallowed functions, please drop a public post on [Piazza](https://piazza.com/umd/fall2019/enae788m). 

<a name='coll'></a>

## 7. Collaboration Policy
<p style="background-color:#ddd; padding:5px">
<b>NOTE:</b> 
You are <b>STRONGLY</b> encouraged to discuss the ideas with your peers. Treat the class as a big group/family and enjoy the learning experience. 
</p>

However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the [ENAE Fall 2019 website](http://prg.cs.umd.edu/enae788m).

<a name='ack'></a>

## 8. Acknowledgements

This data for this fun project was obtained by the ESE 650: Learning In Robotics course at the University of Pennsylvania. 

***
