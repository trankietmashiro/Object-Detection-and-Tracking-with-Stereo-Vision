# Object-Detection-and-Tracking-with-Stereo-Vision
# Stereo Camera Calibration & Object Distance Measurement with YOLO

This project is an enhanced stereo vision system inspired by **TERBOUCHE Hacene's Stereo Calibration** work.  
It not only calibrates and rectifies stereo camera images using OpenCV, but also integrates **YOLO-based object detection** to measure the real-world distance of detected objects.

For detail explaination about stereo vision, please go to TERBOUCHE Hacene's calibration folder which https://github.com/TerboucheHacene/stereo_calibration

---

## Features

- **Stereo Calibration**: Accurate intrinsic and extrinsic parameter estimation for each camera.
- **Stereo Rectification**: Aligns epipolar lines for optimal stereo matching.
- **YOLO Object Detection**: Detects and tracks objects in real-time.
- **3D Distance Measurement**: Computes object distances using stereo disparity and known camera parameters.

---

## System Overview

1. **Stereo Calibration (From TERBOUCHE Hacene)**  
   - Calibrate each camera individually using a chessboard pattern.  
   - Determine the transformation between left and right cameras.  
   - Use `stereoCalibrate` and `initUndistortRectifyMap` in OpenCV to rectify images.

2. **YOLO-based Object Detection**  
   - Run YOLO on the left camera feed.  
   - Detect bounding boxes for objects of interest.  
   - Track objects across frames.

3. **Distance Estimation**  
   - Match detected objects between left and right images.  
   - Compute disparity and use the stereo baseline & focal length to estimate depth.

---

## Installation

It is recommended to use a virtual environment:

```bash
conda create -n stereo_yolo python=3.10
conda activate stereo_yolo

pip install -r requirements.txt
```
