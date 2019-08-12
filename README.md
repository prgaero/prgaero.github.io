# prgaero.github.io
Course materials and notes for University of Maryland's class ENAE788M: Hands On Autonomous Aerial Robotics

## Project 1
#### Project 1a: "Magic" Madgwick Filter for Attitude Estimation 
- Attitude Estimation using [Madgwick Filter](http://x-io.co.uk/res/doc/madgwick_internal_report.pdf) 
#### Project 1b: Non-stinky Unscented Kalman Filter for Attitude Estimation 
- Attitude Estimation using [UKF](https://ieeexplore.ieee.org/document/1257247)
- Collect Data from MPU-9250 IMU (accelerometer and gyroscope values) along with Vicon ground truth 
- Need to align IMU axes with Vicon

## Project 2: Trajectory Following on the PRG Husky 
- Parametrize trajectories as time series and write a simple controller to follow them
- Compare followed trajectory to Vicon estimates
- Need to release trajectory description

## Project 3
#### Project 3a: Mini Drone Race 
- Detect windows of different color and navigate through them
- Need to make the colored windows and release a ROS bag of windows with Vicon poses 
#### Project 3a: Circular Bullseye 
- Estimate relative pose of circular bullseye and land on it
- Need to make the circular bullseye and release a ROS bag of circular bullseye with Vicon poses 

## Project 4
#### Project 4a: Stereo Pose Estimation
- Estimate relative pose of stereo camera from consequtive images
- Need to release a ROS bag of a down facing stereo camera along with IMU data and Vicon pose estimates
- Need to align camera/IMU axes with Vicon

#### Project 4b: Avoid the wall and find the bridge 
- Using pose estimates from down facing stereo camera, estimate sparse/dense depth of front mono camera. Finally use it to avoid the wall in front
- Find the bride using color and Hough transform
- Need to release a ROS bag of down facing stereo camera along with IMU data, front facing mono camera and Vicon pose estimates
- Need to align camera/IMU axes with Vicon and temporally align the data
- Need to release a ROS bag of the bridge data from front and down camera

## Project 5: The Final Race! 
- Race on the track
