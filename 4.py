from cv2 import COLOR_BGR2GRAY
import numpy as np
import cv2
import pixellib
from pixellib.tune_bg import alter_bg
change_bg = alter_bg()
cap = cv2.VideoCapture('1.mp4')

subtractor = cv2.createBackgroundSubtractorMOG2(history=60, varThreshold=50, detectShadows=False)
# subtractor = cv2.createBackgroundSubtractorKNN(history=120, dist2Threshold=100, detectShadows=False)

while True:
    _, frame = cap.read()
    # frame = cv2.cvtColor(frame, COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (9, 9),0)
   
    mask = subtractor.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break    

cap.release()
cv2.destroyAllWindows()