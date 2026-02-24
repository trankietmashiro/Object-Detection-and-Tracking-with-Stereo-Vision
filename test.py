import cv2

capL = cv2.VideoCapture(0, cv2.CAP_V4L2)
capR = cv2.VideoCapture(2, cv2.CAP_V4L2)

print("L:", capL.isOpened())
print("R:", capR.isOpened())

while True:
    retL, frameL = capL.read()
    retR, frameR = capR.read()

    print(retL, retR)

    if not retL or not retR:
        print("Frame grab failed")
        break

    cv2.imshow("Left", frameL)
    cv2.imshow("Right", frameR)

    if cv2.waitKey(1) == 27:
        break

capL.release()
capR.release()
cv2.destroyAllWindows()
