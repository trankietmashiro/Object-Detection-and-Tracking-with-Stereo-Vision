import cv2
import numpy as np
from config import FOCAL_LENGTH, BASELINE, STEREO_CALIB_PATH
from read_calibration import read_stereo_calibration

def compute_disparity_and_depth(frameL, frameR):
    Left_Stereo_Map, Right_Stereo_Map = read_stereo_calibration(STEREO_CALIB_PATH)

    frameLbw = cv2.cvtColor(frameL, cv2.COLOR_BGR2GRAY) if len(frameL.shape) == 3 else frameL
    frameRbw = cv2.cvtColor(frameR, cv2.COLOR_BGR2GRAY) if len(frameR.shape) == 3 else frameR

    left_rect = cv2.remap(frameLbw, *Left_Stereo_Map, interpolation=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT)
    right_rect = cv2.remap(frameRbw, *Right_Stereo_Map, interpolation=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_CONSTANT)

    stereo = cv2.StereoSGBM_create(
        minDisparity=0,
        numDisparities=64,
        blockSize=9,
        P1=8 * 3 * 9**2,
        P2=32 * 3 * 9**2,
        mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
    )
    stereoR = cv2.ximgproc.createRightMatcher(stereo)
    wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=stereo)
    wls_filter.setLambda(80000)
    wls_filter.setSigmaColor(1.8)

    displ = stereo.compute(left_rect, right_rect)
    dispr = stereoR.compute(right_rect, left_rect)
    filtered_disparity = wls_filter.filter(displ, left_rect, disparity_map_right=dispr)

    disparity = filtered_disparity.astype(np.float32) / 16.0
    with np.errstate(divide='ignore'):
        depth = (FOCAL_LENGTH * BASELINE) / disparity
    depth[disparity <= 0] = np.nan
    return depth
