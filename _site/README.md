# cmsc733.github.io
Course materials and notes for University of Maryland's class CMSC733: Computer Vision

## Project 1
- Panorama Stitching
- Supervised Deep Homography
- Unsupervised Deep Homography

## Project 2
- Face Swap using Delaunay Triangulation and TPS  (Facial Landmarks detected using dlib)
- Current ideas for Deep Learning 
  - Implement [Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network](https://arxiv.org/pdf/1803.07835.pdf) to regress 3D mesh of the face and use TPS to warp face and finally poisson blending to blend seamlessly
  - Implement [Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network](https://arxiv.org/pdf/1803.07835.pdf) to regress 3D mesh of the face then implement [Fast Face-swap Using Convolutional Neural Networks](https://arxiv.org/pdf/1611.09577.pdf) based blending using style transfer 


References for Deep Learning 

- [On Face Segmentation, Face Swapping, and Face Perception](https://arxiv.org/pdf/1704.06729.pdf)
- [Fast Face-swap Using Convolutional Neural Networks](https://arxiv.org/pdf/1611.09577.pdf)
- [HeadOn: Real-time Reenactment of Human Portrait Videos](http://niessnerlab.org/projects/thies2018headon.html)
- [Photorealistic Facial Texture Inference Using Deep Neural Networks](https://arxiv.org/pdf/1612.00523v1.pdf)
- [Joint 3D Face Reconstruction and Dense Alignment with Position Map Regression Network](https://arxiv.org/pdf/1803.07835.pdf)
- [Deep Video Portraits](http://gvv.mpi-inf.mpg.de/projects/DeepVideoPortraits/)
- [Deep Fakes](https://www.alanzucconi.com/2018/03/14/introduction-to-deepfakes/)

## Project 3
- Structure from Motion 
  - Feature Extraction and Matching
  - Estimate F (with RANSAC)
  - Estimate E from F (with RANSAC)
  - Check Cheirality condition and Triangulation
  - Linear PnP
  - Non Linear PnP
  - Bundle Adjustment
  - Plot Camera Poses and 3D Structure
- [SfM Learner](https://people.eecs.berkeley.edu/~tinghuiz/projects/SfMLearner/)
  - Depth Scale Alignment using predicted pose
  - Plot Camera Poses and 3D Structure
  
## Project 4
- Reconstruct 3D Scene using Point to Plane ICP on RGBD data
- Implement [SharpMask?](https://arxiv.org/abs/1603.08695) to obtain segmentation in 2D
- Fuse outputs of SharkMask in 3D?

