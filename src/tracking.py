import cv2
from stereo_depth import compute_disparity_and_depth
from config import tracker, classNames, model
import numpy as np

def get_bbox_depth(depth_map, bbox):
    x1, y1, x2, y2 = map(int, bbox)
    region = depth_map[y1:y2, x1:x2]
    valid = region[np.isfinite(region)]
    return np.median(valid) if valid.size > 0 else None

def process_frame(frameL, frameR):
    results = model(frameL)
    detections = []

    for result in results[0].boxes:
        x1, y1, x2, y2 = result.xyxy[0].tolist()
        cls = int(result.cls[0])
        confidence = result.conf[0].item()
        class_id = result.cls[0].item()

        if confidence > 0.8:
            width = x2 - x1
            height = y2 - y1
            detections.append(([int(x1), int(y1), int(width), int(height)], confidence, int(class_id)))
    
    track_id_to_class = {}
    track_id_to_unique_id = {}
    class_id_counts = {}

    # Update tracks
    tracks = tracker.update_tracks(detections, frame=frameL)
    
    # Compute disparity/depth map once
    depth_map = compute_disparity_and_depth(frameL, frameR)

    for track in tracks:
        if not track.is_confirmed() or track.time_since_update > 1:
            continue
        
        bbox = track.to_tlbr()
        track_id = track.track_id

        # Get class name safely
        if cls is not None and cls < len(classNames):
            class_name = classNames[cls]
        else:
            class_name = "Unknown"

        # Assign class label to track ID
        if track_id not in track_id_to_class:
            track_id_to_class[track_id] = class_name

        class_label = track_id_to_class[track_id]

        # Assign a unique ID per class
        if class_label not in class_id_counts:
            class_id_counts[class_label] = 1
        else:
            class_id_counts[class_label] += 1

        if track_id not in track_id_to_unique_id:
            unique_id = f"{class_label}{class_id_counts[class_label]}"
            track_id_to_unique_id[track_id] = (class_label, class_id_counts[class_label])

        # Draw bounding box
        cv2.rectangle(frameL, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 255, 0), 2)

        # Get depth for bounding box
        object_distance = get_bbox_depth(depth_map, bbox)

        # Draw label
        if object_distance is not None:
            label = f"{class_label} ID:{track_id_to_unique_id[track_id][1]} Dist:{object_distance:.2f}m"
        else:
            label = f"{class_label} ID:{track_id_to_unique_id[track_id][1]} Dist:N/A"

        cv2.putText(frameL, label, (int(bbox[0]), int(bbox[1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frameL
