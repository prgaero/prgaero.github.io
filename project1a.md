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
In this project, you will implement a Madgwick filter to estimate the three dimensional orientation/attitude. You are given data from an [ArduIMU+ V2](https://www.sparkfun.com/products/retired/9956) six degree of freedom Inertial Measurement Unit (6-DoF IMU) sensor i.e. readings from a 3-axis gyroscope and a 3-axis accelerometer. You will estimate the underlying 3D orientation and compare it with the ground truth data given by a [Vicon motion capture system](https://www.vicon.com/).

<a name='data'></a>
## 3. Reading the Data
The `Data` folder has two subfolders, one which has the raw IMU data `Data\Train\IMU` and another one which has the Vicon data `Data\Train\Vicon`. The data in each folder is numbered for correspondence, i.e., `Data\Train\IMU\imuRaw1.mat` corresponds to `Data\Train\Vicon\viconRot1.mat`. Download the data from [here](https://drive.google.com/file/d/14iIGleYdRmsQFgz5P0feKpW_tkLJ1r9m/view?usp=sharing). These data files are given in a `.mat` format. In order to read these files in Python, use the snippet provided below:

```
>>> from scipy import io
>>> x = io.loadmat("filename.mat")
```

This will return data in a dictionary format. Please disregard the following keys and corresponding values: `__version__`, `__header__`, `__global__`. The keys: `vals` and `ts` are the main data you need to use. `ts` are the timestamps and `vals` are values from the IMU. Each column of `vals` denotes data in the following order: $$ \begin{bmatrix} a_x & a_y & a_z & \omega_z & \omega_x & \omega_y\end{bmatrix}^T$$. Note that these values are not in physical units and need to undergo a convertion. 

To convert the acceleration values to $$ms^{-2}$$, follow these steps. 

$$  
\tilde{a_x} = \frac{a_x + b_{a,x}}{s_x} \\
$$

Follow the same steps for $$a_y$$ and $$a_z$$. Here $$\tilde{a_x}$$ represents the value of $$a_x$$ in physical units, $$b_{a,x}$$ is the bias and $$s_x$$ is the scale factor of the accelerometer. 

To read accelerometer bias and scale parameters, load the `Data\IMUParams.mat` file. `IMUParams` is a $$2 \times 3$$ vector where the first row denotes the scale values $$\begin{bmatrix} s_x & s_y & s_z \end{bmatrix}$$. The second row denotes the biases (computed as the average biases of all sequences using vicon) $$\begin{bmatrix} b_{a, x} & b_{a, y} & b_{a, z} \end{bmatrix}$$. 

To convert $$\omega$$ to $$rads^{-1}$$, 

$$
\tilde{\omega} = \frac{3300}{1023} \times \frac{\pi}{180} \times 0.3 \times \left(\omega - b_{g}\right)
$$

Here, $$\tilde{\omega}$$ representes the value of $$\omega$$ in physical units and $$b_g$$ is the bias. $$b_g$$ is calculated as the average of first few hundred samples (assuming that the IMU is at rest in the beginning). 

From the Vicon data, you will need the following 2 keys: `ts` and `rots`. `ts` is the timestamps of size $$1 \times N$$ as before and `rots` is a $$3\times 3\times  N$$ matrix denoting the `Z-Y-X` Euler Angles rotation matrix estimated by Vicon. 

An image of the rig used for data collection is shown below:

<div class="fig fighighlight">
  <img src="/assets/2019/p1/IMURig.png" width="100%">
  <div class="figcaption">
    Figure 1: IMU Rig used for data collection.
  </div>
  <div style="clear:both;"></div>
</div>


<a name='calib'></a>
## 4. Sensor Calibration
Note that the registation between the IMU coordinate system and the Vicon global coordinate system might not be aligned at start. You might have to align them. 

The Vicon and IMU data are NOT hardware syncronized, although the timestamps `ts` of the respective data are correct. Use `ts` as the reference while plotting the orientation from Vicon and IMU. You can also do a software stncronization using the time stamps. You can align the data from the two closest timestamps from IMU and Vicon data respectively.


<a name='implementation'></a>
## 5. Implementation


1. You will write a function that computes orientation only based on gyro data (using integration, assume that you know the initial orientation from Vicon). Check if that works well. Plot the results and verify. Add the plot to your report file.
2. You will write another function that computes orientation only based on accelerometer data (assume that the IMU is only rotating). Verify if that function works well before you try to integrate them into a single filter. THIS IS VERY IMPORTANT! Add the plot to your report file.
3. Now, write a function for Madgwick filter that computes orientation based on gyroscope and accelerometer data only. Make sure you plot the orientation in all axis and compare with Vicon plots. Show the plot in your report as well.

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

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder and should of a conference quality paper. Feel free to use any online tool to edit such as [Overleaf](https://www.overleaf.com) or install LaTeX on your local machine.
- Link to the `rotplot` videos comparing attitude estimation using Gyro Integration, Accelerometer Estimation, Madgwick Filter and Vicon. Sample video can be seen [here](https://www.youtube.com/watch?feature=player_embedded&v=iCe3o-9moUM).
- Plots for all the train and test sets. In each plot have the angles estimated from gyro only, accelerometer only, madgwick filter and Vicon along with proper legend.  
- A sample report for a similar project is given in the `.zip` file given to you with the name `SampleReport.pdf`. Treat this report as the benchmark or gold standard which we'll compare your reports to for grading.

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

However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the [ENAE 788M Fall 2019 website](http://prg.cs.umd.edu/enae788m).

<a name='ack'></a>

## 10. Acknowledgements

This data for this fun project was obtained by the ESE 650: Learning In Robotics course at the University of Pennsylvania. 

***
