import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# import pixellib
# from pixellib.tune_bg import alter_bg
img = cv.imread('bum3.jpg')
imgbg = cv.imread('bg.jpg')
cv.imshow("Paling Awal", img)
mask = np.zeros(img.shape[:2],np.uint8)
print(str(img.shape[:2]))
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
h,w,i = img.shape
rect = (1,1,w,h)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,20,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
cv.imshow("Backgorund Hitam", img)
resizeBack = cv.resize(imgbg, (w, h), interpolation = cv.INTER_CUBIC)
for i in range(w):
    for j in range(h):
        pixel = img[j, i]
        if np.all(pixel == [0, 0, 0]):
            img[j, i] = imgbg[j, i] 
cv.imshow("Background Ganti", img)

cv.waitKey(0)
cv.destroyAllWindows()