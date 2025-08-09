from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import torch

YOLO_MODEL_PATH = 'yolov8n.pt'
STEREO_CALIB_PATH = r"D:\Desktop\stereo\calib_data\params\stereo_calibration.xml"
FOCAL_LENGTH = 572  # pixels
BASELINE = 0.006  # meters

model = YOLO(YOLO_MODEL_PATH)
model.to("cuda" if torch.cuda.is_available() else "cpu")
tracker = DeepSort(max_age=30, nn_budget=100)

# Class names as given in your example
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light", 
              "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow",
              "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", 
              "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
              "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange",
              "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cellphone", "microwave", 
              "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier",
              "toothbrush"]
