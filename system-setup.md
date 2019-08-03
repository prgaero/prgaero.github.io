---
layout: page
title: System Setup
permalink: /system-setup/
---

## System Setup for local machines:

This is the system setup instructions for CMSC733 class for local machines. We <b>ONLY</b> support Ubuntu-16.04. Feel free to use a Virtual Machine on your system if you don't an Ubuntu machine. We <b>STRONGLY</b> recommend [Virtual Box](https://www.virtualbox.org/wiki/Downloads) as a virtual machine monitor.

### 1. Install OpenCV-3.4:

Due to certain issues in `opencv-4`, we have decided to revert back to `opencv3` for this course. After the latest release, the 'right' way to install `opencv-3` is to `build` from source. Feel free to follow the official documentation for version `3.4.0` if you want or follow the given steps:

```
sudo apt update
sudo apt upgrade
```

Go to [this github page](https://github.com/chahatdeep/ubuntu-for-robotics/tree/master/CMSC733) and download the two shell scripts:
- [install_opencv3-Part1.sh](https://github.com/chahatdeep/ubuntu-for-robotics/blob/master/CMSC733/install_opencv3-Part1.sh)
- [install_opencv3-Part2.sh](https://github.com/chahatdeep/ubuntu-for-robotics/blob/master/CMSC733/install_opencv3-Part2.sh)

Do: 
```
sudo chmod u+x install_opencv3-Part1.sh install_opencv3-Part2.sh
./install_opencv3-Part1.sh
```

If it outputs an error, please read the lines `33-36` from `install_opencv3-Part1.sh` to tackle the problem (hopefully).
If it works, perfectly fine, do:
```
install_opencv3-Part2.sh
```


Now, check the OpenCV version by opening `python` console and do the following:

```
import cv2
cv2.__version__
```

It must be `3.4.0`.

Please feel free to use any other sources for installation and try to avoid `virtualenv` and `conda` if possible. 

***

### 2. Python Dependencies:

```
sudo apt install python-numpy python-scipy python-scikits-learn python-matplotlib python-skimage python-pil
```

```
sudo -H pip install termcolor tqdm
```



### 3. TensorFlow (CPU version)

If you have GPU's that don't support NVIDIA `CUDA`, install the CPU version for tensorflow

```
sudo -H pip install tensorflow
```

### 4. TensorFlow (GPU version)

If you have NVIDIA 970 or later, using gpu version of tensorflow is recommended.


#### <b>A.</b> Install NVIDIA drivers, if you don't have one.

```
sudo apt install nvidia-smi nvidia-384
```
--- or --- 

```
sudo apt install nvidia-smi nvidia-396
```
<br>

#### <b>B.</b> Download and install `CUDA-9.0` : (File size is 1.1GB)

```
cd ~/Downloads/
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb
mv -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64-deb cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb 
sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub
sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb 
sudo apt-get update
sudo apt-get install cuda
sudo apt install nvidia-cuda-toolkit
nvcc --version
```


- If you see Cuda compilation tools version (`nvcc --version`) as `7.5` instead of `cuda-9.0`, do: 

```
echo 'export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}' >> ~/.bashrc
source ~/.bashrc
```

- Check `nvcc --version` again. It should show you `cuda-9.0`.
<br><br>

#### <b>C.</b> CuDNN Installation:

- Download `cudnn-7.4` (for `cuda-9.0` ) [here](https://drive.google.com/open?id=1xWPfS8xaxdUHeiZQbdMGr0R3sPfOdNfp). The file is 347 MB.

```
# install cuDNN v7.4
CUDNN_TAR_FILE="cudnn-9.0-linux-x64-v7.4.1.5.tgz"
tar -xzvf ${CUDNN_TAR_FILE}
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-9.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-9.0/lib64/
sudo chmod a+r /usr/local/cuda-9.0/lib64/libcudnn*
```
```
# set environment variables
export PATH=/usr/local/cuda-9.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

#### <b>D.</b> TensorFlow GPU package installation:
```sudo -H pip install tensorflow-gpu```


***

## Google Cloud Platform Setup
(Coming Soon)





