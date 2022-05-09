import numpy as np
import cv2 as cv
cap = cv.VideoCapture('1.mp4')
#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
fgbg = cv.createBackgroundSubtractorMOG2()
while True:
    ret,frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
 #   fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(cap.get(cv.CAP_PROP_POS_FRAMES)), (15, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    cv.imshow('Frame', frame)
    cv.imshow('FG MASK Frame', fgmask)


    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cap.release()
cv.destroyAllWindows()