---
layout: page
mathjax: true
title: Magic Madgwick Filter for Attitude Estimation 
permalink: /2019/proj/p1a/
---

Table of Contents:
- [1. Deadline](#due)
- [2. Problem Statement](#prob)
- [3. Reading the data](#data)
- [4. Sensor Calibration](#calib)
- [5. Implementation](#implementation)
- [6. Notes About Test Set](#testset)
- [7. Submission Guidelines](#sub)
  - [7.1. File tree and naming](#files)
  - [7.2. Report](#report)
- [8. Allowed and Disallowed functions](#funcs)
- [9. Collaboration Policy](#coll)
- [10. Acknowledgements](#ack)

<a name='due'></a>
## 1. Deadline 
**11:59 PM, September 10, 2019.**

<a name='prob'></a>
## 2. Problem Statement 
In this project, you will implement a Madgwick filter to track three dimensional orientation. Given IMU sensor readings from a 3-axis gyroscope and a 3-axis accelerometer (6-DoF IMU), you will estimate the underlying 3D orientation and compare it with the ground truth data given by a [Vicon motion capture system](https://www.vicon.com/). 

<a name='data'></a>
## 3. Reading the Data
The `Data` folder has two subfolders, one which has the raw IMU data `Data\IMU` and aonther one which has the Vicon data `Data\Vicon`. The data in each folder is numbered for correspondence, i.e., `Data\IMU\imuRaw1.mat` corresponds to `Data\Vicon\viconRot1.mat`. Download the data from [here](Data-Link). These data files are given in a `.mat` format. In order to read these files in Python:

```
>>> from scipy import io
>>> x = io.loadmat("filename.mat")
```

This will return in a dictionary format. Please disregard the following keys and corresponding values: `__version__`, `__header__`, `__global__`. The keys: `vals` and `ts` are the main data you need to use. `ts` are the timestamps and `vals` are values from the IMU in the specific order: $$a_x$$, $$a_y$$, $$a_z$$, $$\omega_z$$, $$\omega_x$$, $$\omega_y$$. Note that these values are not in physical units and need to undergo a convertion. 

To convert the acceleration values to $$ms^{-2}$$, follow these steps. 

$$  
\tilde{a_x} = \frac{a_x + b_{a,x}}{s_x} \\
$$

Follow the same steps for $$a_y$$ and $$a_z$$. Here $$\tilde{a_x}$$ represents the value of $$a_x$$ in physical units, $$b_{a,x}$$ is the bias and $$s_x$$ is the scale factor. 

To read accelerometer bias and scale paramteres, load the `Data\IMUParams.mat` file. `IMUParams` is a $$2 \times 3$$ vector where the first row denotes the scale values $$\begin{bmatrix} s_x & s_y & s_z \end{bmatrix}$$. The second row denotes the biases (computed as the average biases of all sequences using vicon) $$\begin{bmatrix} b_{a, x} & b_{a, y} & b_{a, z} \end{bmatrix}$$. 

To convert $$\omega$$ to $$rads^{-1}$$, 

$$
\tilde{\omega} = \frac{3300}{1023} \times \frac{\pi}{180} \times 0.3 \times \left(\omega - b_{g}\right)
$$

Here, $$\tilde{\omega}$$ representes the value of $$\omega$$ in physical units and $$b_g$$ is the bias.

<a name='calib'></a>
## 4. Sensor Calibration
Note that the registation between the IMU coordinate system and Vicon global coordinate system might not be aligned at start. You might have to align them. 

The Vicon and IMU data are exactly synced, although the timestamps `ts` of the respective data are correct. Use `ts` as the reference while plotting the orientation from Vicon and IMU. 

ALSO TIME SYNC!!!!!

<a name='implementation'></a>
## 5. Implementation

You will write a function that computes orientation only based on gyro data (using integration, assume that you know the initial orientation from Vicon), and another function that computes orientation only based on accelerometer data (assume that the IMU is only rotating). You should check that each function works well before you try to integrate them into a single filter. This is very important!

Then you will write a function for madgwick filter that computes orientation based on gyroscope and accelerometer data only. Make sure you plot the orientation in all axis and compare with Vicon plots.

In the starter code, a function called `rotplot.py` is also included. Use this function to visualize the orientation of your output. To plot the orientation, you need to give a $$3 \times 3$$ rotation matrix as an input.


<a name='testset'></a>
## 6. Notes About Test Set
A test set will be released 24 hours before the deadline. You can download the test set from <b>here</b>. Your report MUST include the output from both the train and test sets. 

<a name='sub'></a>

## 7. Submission Guidelines

**If your submission does not comply with the following guidelines, you'll be given ZERO credit.**

### 7.1. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``YourDirectoryID_p1a.zip``. If you email ID is ``abc@umd.edu`` or ``abc@terpmail.umd.edu``, then your ``DirectoryID`` is ``abc``. For our example, the submission file should be named ``abc_p1a.zip``. The file **must have the following directory structure**. The file to run for your project should be called ``YourDirectoryID_p1a/Code/Wrapper.py``. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. 

<p style="background-color:#ddd; padding:5px">
<b>NOTE:</b> 
Please <b>DO NOT</b> include data in your submission. Furthermore, the size of your submission file should <b>NOT</b> exceed more than <b>20MB</b>.
</p>

The file tree of your submission <b>SHOULD</b> resemble this:

```
YourDirectoryID_p1a.zip
├── Code
|   ├── Wrapper.py
|   └── Any subfolders you want along with files
├── Report.pdf
└── README.md
```

<a name='report'></a>

### 7.2. Report

For each section of the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented. You must include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder and should of a conference quality paper.

<a name='funcs'></a>

## 8. Allowed and Disallowed functions

<b> Allowed:</b>

- Any functions regarding reading, writing and displaying/plotting images in `cv2`, `matplotlib`
- Basic math utitlies including convolution operations in `numpy` and `math`
- Any functions for pretty plots
- Quaternion libraries
- Any library that perform tranformation between various representations of attitude

<b> Disallowed:</b>

- Any function that implements in-part or full Madgwick filter

If you have any doubts regarding allowed and disallowed functions, please drop a public post on [Piazza](https://piazza.com/umd/fall2019/enae788m). 

<a name='coll'></a>

## 9. Collaboration Policy

<p style="background-color:#ddd; padding:5px">
<b>NOTE:</b> 
You are <b>STRONGLY</b> encouraged to discuss the ideas with your peers. Treat the class as a big group/family and enjoy the learning experience. 
</p>

However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the [ENAE Fall 2019 website](http://prg.cs.umd.edu/enae788m).

<a name='ack'></a>

## 10. Acknowledgements

This fun project was inspired by our research in <a href="http://prg.cs.umd.edu/">Perception and Robotics Group</a> at University of Maryland, College Park.

***
