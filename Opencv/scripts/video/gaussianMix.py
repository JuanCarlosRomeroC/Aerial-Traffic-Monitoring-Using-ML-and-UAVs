import os
import cv2 as cv

cap = cv.VideoCapture('vtest.mp4')
fgbg = cv.bgsegm.createBackgroundSubtractorMOG(history=10000)
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()




