import cv2
import numpy as np

cap = cv2.VideoCapture("./vStream.h264")
count = 0

while True:
    ret, frame = cap.read()
    if ret:
        print("Decoded frame")
        # cv2.imshow("frame", frame)
        cv2.imwrite("fr_"+str(count)+".png", frame)
        count += 1
    else:
        print("Couldn\'t decoded frame") 
