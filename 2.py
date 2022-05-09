# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('1.mp4')
# #kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
# fgbg = cv.createBackgroundSubtractorMOG2()

# 	#if ret is true than no error with cap.isOpened
# ret, frame = cap.read()
	
# while True:
#     if ret==True:

#         #apply background substraction
#         fgmask = fgbg.apply(frame)
                        
#         #check opencv version
#         contours, hierarchy = cv.findContours(fgmask.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
            
#             #looping for contours
#         for c in contours:
#             if cv.contourArea(c) < 500:
#                 continue
                    
#                 #get bounding box from countour
#             (x, y, w, h) = cv.boundingRect(c)
                
#                 #draw bounding box
#             cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
#         cv.imshow('foreground and background',fgmask)
#         cv.imshow('rgb',frame)
#         if cv.waitKey(1) & 0xFF == ord("q"):
#             break


# cap.release()
# cv.destroyAllWindows()


import numpy as np
import cv2
import sys

    
version = cv2.__version__.split('.')[0]

#read video file
cap = cv2.VideoCapture('1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

#check opencv version


while (cap.isOpened):

	#if ret is true than no error with cap.isOpened
	ret, frame = cap.read()
	if frame is None:
		break

		#apply background substraction

	fgmask = fgbg.apply(frame)
					
	contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		
		#looping for contours
	for c in contours:
		if cv2.contourArea(c) < 500:
			continue
				
			#get bounding box from countour
		(x, y, w, h) = cv2.boundingRect(c)
			
			#draw bounding box
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			
	cv2.imshow('foreground and background',fgmask)
	cv2.imshow('rgb',frame)
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break


cap.release()
cv2.destroyAllWindows()