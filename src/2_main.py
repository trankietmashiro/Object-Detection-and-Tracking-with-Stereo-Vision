import cv2
from tracking import process_frame

def process_stream():
    capL, capR = cv2.VideoCapture(1), cv2.VideoCapture(2)
    if not capL.isOpened() or not capR.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        retR, frameR = capR.read()
        retL, frameL = capL.read()
        if not (retR and retL): break

        frame = process_frame(frameL, frameR)
        cv2.imshow('Object Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): break

    capL.release()
    capR.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_stream()
