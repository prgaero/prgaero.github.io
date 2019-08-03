---
layout: page
mathjax: true
title: Learning the Structure from Motion | An Unsupervised Approach
permalink: /2019/proj/p4/
---

**To be submitted in a group.**

**YOU CANNOT USE LATE DAYS FOR THIS PROJECT**


Table of Contents:
 
- [1. Deadline](#due)
- [2. Introduction](#intro)
- [3. SfMLearner](#sfmlearner)
- [4. Notes about the dataset](#dataset)
  - [4.1. Note about the SfMLearner Code](#code)
- [5. Submission Guidelines](#sub)
  - [5.1. File tree and naming](#files)
  - [5.2. Report](#report)
  - [5.3. Video Presentation](#video)
- [6. Collaboration Policy](#coll)


<a name='due'></a>

## 1. Deadline 

**11:59PM, May 18, 2019.**

<a name='intro'></a>

## 2. Introduction

We have dealt with reconstructing 3D structure of a given scene using images from multiple views using the traditional (geometric) approach. Though, there is a possibility of achieving more robust results. In this project, we will learn about estimating depth and pose (or ego-motion) from a sequence of images using unsupervised learning methods. In [SfMLearner](https://people.eecs.berkeley.edu/~tinghuiz/projects/SfMLearner/cvpr17_sfm_final.pdf) paper by David Lowe's team at Google, an unsupervised learning framework was presented for the task of monocular depth and camera motion estimation from unstructured video sequences. 

Your task is to make [SfMLearner](https://people.eecs.berkeley.edu/~tinghuiz/projects/SfMLearner/cvpr17_sfm_final.pdf) 'better'! When we say better, it means that the error in depth and pose estimation must be less than that of SfMLearner's paper on different empirical evaluation scales. Research papers like [GeoNet](https://arxiv.org/pdf/1803.02276.pdf) might help you in improving the results. Although, research papers in this field are in abundance. Feel free to search through the internet. 

You will be mainly graded on the analysis of your approach and 'your original' implementation to make the SfMLearner better! You are encouraged to **change the architecture, loss function and augement the data**. Along with the standard report, you will be submitting a presentation video of about 5-7 mins long, explaining your approach and the in-depth analysis of your methods and the results. More on submission details are mentioned below in [section 5](#sub).

Note: You don't have to reimplement SfMLearner again! You will be not graded for that. Use the SfMLearner code on [Github](https://github.com/tinghuiz/SfMLearner) by the original authors. Feel free to modify the SfMLearner code. **You are not allowed to use any online code except SfMLearner that involves any kind of 'deep learning' (apart from your previous projects).** Although, **feel free to use ANY traditional computer vision open source program or toolbox.** DO NOT forget to cite them. You are restricted to $$\sim$$ 12K images provided in the dataset for training.
**NOTE:** You have to retrain the SfMLearner on the 12K images (rather than getting numbers from the paper) to have a fair comparison with your method. More on the dataset is given in [section 4](#dataset)


<a name='sfmlearner'></a>

## 3. SfMLearner

One of the trivial ways to solve this problem is to learn rotation and translation from a sequence of data. Although, learning such parameters directly is a weakly constrained problem. Thus, methods like [SfMLearner](https://people.eecs.berkeley.edu/~tinghuiz/projects/SfMLearner/cvpr17_sfm_final.pdf), jointly train a single-view depth CNN and a camera pose estimation CNN from unlabeled video sequence. <b>Assumption: The scene is fairly rigid <i>i.e.</i> the scene appearance change across different frames is dominated by the camera motion.</b>

<b> You are required to read [SfMLearner](https://people.eecs.berkeley.edu/~tinghuiz/projects/SfMLearner/cvpr17_sfm_final.pdf) paper to work on this project. </b>


<a name='dataset'></a>

## 4. Notes about Data

You are given a multiple sequences from the [KITTI](http://www.cvlibs.net/datasets/kitti/raw_data.php) dataset. You can download the training data (and validation) from [here](https://drive.google.com/file/d/1A1BtjeZW5p7FQGovjd5sySYusOEZy8Vl/view?usp=sharing). Also, you can download the testing dataset from here: [KITTI Testing set]().
Training set is available now. Testing set will be online soon. 

<a name='code'></a>

### 4.1 Note about the SfMLearner Code

The code provided in their [official Github repository](https://github.com/tinghuiz/SfMLearner) may not work out of the box. 
In case you have error, like "num_source is not defined", please download the updated `train.py` file from [here](assets/2019/p4/train.py) and replace it with in the original `train.py`. It is the same file with a few flags changed.

For the rest of the code, please follow their official github repo!


<a name='sub'></a>

## 5. Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit </b>

<a name='files'></a>

### 5.1. File tree and naming

Your submission on ELMS/Canvas must be a ``zip`` file, following the naming convention ``YourDirectoryID_p4.zip``. If you email ID is ``abc@umd.edu`` or ``abc@terpmail.umd.edu``, then your ``DirectoryID`` is ``abc``. For our example, the submission file should be named ``abc_p1.zip``. The file **must have the following directory structure** because we'll be autograding assignments. You can have any helper functions in sub-folders as you wish, be sure to index them using relative paths and if you have command line arguments for your Wrapper codes, make sure to have default values too. Please provide detailed instructions on how to run your code in ``README.md`` file. Please **DO NOT** include data in your submission.

```
YourDirectoryID_hw1.zip
│   README.md
|   Code 
|   ├── Train.py
|   ├── Test.py
|   └── Any subfolders you want along with files 
|   Data
|   └── AnyOutputImagesYouWantToHighlight.png
├── Models
|   ├── SfMLearnerTrainedModelFiles
|   └── YourMethodTrainedModelFiles
├── Report.pdf
└── PresentationVideo.mp4
```
<a name='report'></a>

### 5.2. Report

For each section of newly developed solution in the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented.  You must include the following details in your writeup:

- Your report **MUST** be typeset in LaTeX in the IEEE Tran format provided to you in the ``Draft`` folder and should of a conference quality paper.
- Brief explanation of your approach to this problem. Talk about the architectural and loss function changes. Also, talk about how you augmented the data.
- Present a set of images for comparison of depth estimation of SfMLearner, YourMethod and Ground Truth (with the input RGB image).
- Present a odometry comparison of pose estimation of SfMLearner, YourMethod and Ground Truth.
- Present a comparison of error of SfMLearner and YourMethod in different error metric scale (Abs, Sq, RMSE and RMSE log) as mentioned in the paper. The scripts for computing error metrics for both pose and depth evaluation can be downloaded from [here](https://github.com/tinghuiz/SfMLearner/tree/master/kitti_eval). For this, train ONLY on the KITTI training set provided here and test it on [KITTI testing set]().
- Present Training Accuracy on the provided KITTI training set. Present Testing accuracy on the provided KITTI testing set.
- Present an in-depth analysis of your proposed approach. Did you try something specific? If yes, why? Talk about why it performed better or worse?
- Present a 3D structure of the scene, reconstructed from depth and poses estimated. Feel free to directly use parts of your project 3 or any open source code for this.    


<a name='video'></a>

### 5.3 Video Presentation

You are required to submit a video explaining your approach to the given problem. Explain what all problems you tackled during this problem and how you overcame them. Also, give an in-depth analysis of your proposed approach. The video MUST be less 7 mins long. We expect the video to be in somewhere between 5-7 mins.


<a name='coll'></a>

## 6. Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the CMSC733 Spring 2019 website.
