import cv2
from tracking import process_frame

def process_stream():
    capL = cv2.VideoCapture(0, cv2.CAP_V4L2)
    capR = cv2.VideoCapture(2, cv2.CAP_V4L2)

    print("Left:", capL.isOpened())
    print("Right:", capR.isOpened())

    if not capL.isOpened() or not capR.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        retR, frameR = capR.read()
        retL, frameL = capL.read()
        if not (retR and retL):
            break

        frame = process_frame(frameL, frameR)
        cv2.imshow('Object Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capL.release()
    capR.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_stream()
