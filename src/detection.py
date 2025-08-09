from config import model
import torch 

model.to("cuda" if torch.cuda.is_available() else "cpu")

def detect_objects(frameL):
    results = model(frameL)
    detections = []
    for result in results[0].boxes:
        x1, y1, x2, y2 = result.xyxy[0].tolist()
        confidence = result.conf[0].item()
        class_id = int(result.cls[0])
        if confidence > 0.8:
            width, height = x2 - x1, y2 - y1
            detections.append(([int(x1), int(y1), int(width), int(height)], confidence, class_id))
    return detections
