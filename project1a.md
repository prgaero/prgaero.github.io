---
layout: page
mathjax: true
title: MyAutoPano
permalink: /2019/proj/p1a/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)


- [8. Submission Guidelines](#sub)
  - [8.1. Starter Code](#starter)
  - [8.2. File tree and naming](#files)
  - [8.3. Report](#report)
- [9. Allowed and Disallowed functions](#funcs)
- [10. Collaboration Policy](#coll)
- [11. Acknowledgements](#ack)

<a name='due'></a>
## 1. Deadline 
**11:59 PM, Thursday, February 21, 2019.**

<a name='prob'></a>
## 2. Problem Statement 
In this project, you will implement a Madgwick filter to track three dimensional orientation. Given IMU sensor readings from gyroscopes and accelerometers, you will estimate the underlying 3D orientation and compare it with the ground truth data given by a Vicon motion capture system. 

<a name='data'></a>
## 3. Reading the Data
You will find a set of IMU data, another set of data that gives the corresponding tracking information from the Vicon motion capture system.
Dowload the data from [here](Data-Link). The files are given in a `.mat` format. In order to read these files in Python:

```
>>> from scipy import io
>>> x = io.loadmat("filename.mat")
```

This will return in a dictionary format. Please disregard the following keys and corresponding values: `__version__`, `__header__`, `__global__`. The keys: `vals` and `ts` are the main data you need to use. `ts` are the timestamps and `vals` are values from the IMU in the specific order: `a_x`, `a_y`, `a_z`, \\\omega_x\\, \\\omega_y\\, \\\omega_z\\. 

<a name='calib'></a>
## 4. Sensor Calibration
Note that the biases and scale factors of the IMU sensors are unknown as well as the registation between the IMU coordinate system and Vicon global coordinate system. You will have to figure them out.


<a name='implementation'></a>
## 5. Implementation
You will write a function that computes orientation only based on gyro data, and another function that computes orientation only based on accelerometer data. You should check that each function works well before you try to integrate them into a single filter. This is very important!
Then you will write a function for madgwick filter that computes orientation based on gyroscope and accelerometer data only. Make sure you plot the orientation in all axis and compare with Vicon plots.


<a name='sub'></a>

## 6. Submission Guidelines

**If your submission does not comply with the following guidelines, you'll be given ZERO credit.**

### 6.1. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``YourDirectoryID_p1a.zip``. If you email ID is ``abc@umd.edu`` or ``abc@terpmail.umd.edu``, then your ``DirectoryID`` is ``abc``. For our example, the submission file should be named ``abc_p1a.zip``. The file **must have the following directory structure**. The file to run for your project should be called ``YourDirectoryID_p1a/Code/Wrapper.py``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. 

<p style="background-color:#ddd; padding:5px">
<b>NOTE:</b> 
Please <b>DO NOT</b> include data in your submission. Furthermore, the size of your submission file should <b>NOT</b> exceed more than <b>20MB</b>.
</p>

The file tree of your submission <b>SHOULD</b> resemble this:

```
YourDirectoryID_p1.zip
├── Code
|   ├── Wrapper.py
|   └── Any subfolders you want along with files
├── Report.pdf
└── README.md
```

<a name='report'></a>

### 6.2. Report

For each section of the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented. You must include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder and should of a conference quality paper.

<a name='funcs'></a>

## 7. Allowed and Disallowed functions

<b> Allowed:

- Any functions regarding reading, writing and displaying/plotting images in `cv2`, `matplotlib`
- Basic math utitlies including convolution operations in `numpy` and `math`
- Any functions for pretty plots
- Any functions for filtering and implementing gaussian blur

<b> Disallowed:

- *Add disallowed* functions!

If you have any doubts regarding allowed and disallowed functions, please drop a public post on [Piazza](https://piazza.com/umd/fall2019/enae788m). 

<a name='coll'></a>

## 10. Collaboration Policy
<p style="background-color:#ddd; padding:5px">
<b>NOTE:</b> 
You are <b>STRONGLY</b> encouraged to discuss the ideas with your peers. Treat the class as a big group/family and enjoy the learning experience. 
</p>

However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the [CMSC733 Fall 2019 website](http://prg.cs.umd.edu/enae788m).

<a name='ack'></a>

## 11. Acknowledgements

This fun project was inspired by our research in <a href="http://prg.cs.umd.edu/">Perception and Robotics Group</a> at University of Maryland, College Park.

***
