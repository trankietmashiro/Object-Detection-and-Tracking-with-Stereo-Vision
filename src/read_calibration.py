import cv2
import numpy as np
from typing import Tuple

def read_stereo_calibration(xml_path: str) -> Tuple[Tuple[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]:
    fs = cv2.FileStorage(xml_path, cv2.FILE_STORAGE_READ)
    if not fs.isOpened():
        raise FileNotFoundError(f"Cannot open calibration file: {xml_path}")
    
    left_map = fs.getNode("stereo_map_left_x").mat(), fs.getNode("stereo_map_left_y").mat()
    right_map = fs.getNode("stereo_map_right_x").mat(), fs.getNode("stereo_map_right_y").mat()
    fs.release()

    if left_map[0] is None or right_map[0] is None:
        raise ValueError("Stereo calibration maps are missing or corrupted.")
    return left_map, right_map
