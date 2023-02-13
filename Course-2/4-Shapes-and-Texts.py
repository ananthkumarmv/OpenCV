import cv2 as cv
import numpy as np


blank = np.zeros((512, 512, 3))
cv.imshow('Blank Image', blank)

# blank[:] = [255, 0, 0]

# 1. Drawing line 
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=2)
cv.imshow('Line', blank)

# 2. Drawing rectangle
cv.rectangle(blank, (blank.shape[1]//2 - 100, blank.shape[0]//2 - 100), ((blank.shape[1]//2 + 100, blank.shape[0]//2 + 100)), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

# 3. Drawing circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (255, 0, 0), thickness=2)
cv.imshow('Circle', blank)

# 4. Writing text 
cv.putText(blank, 'Origin', (0, 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 0)
cv.putText(blank, 'center', (blank.shape[1]//2, blank.shape[0]//2), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 0)
cv.imshow('Text', blank)




cv.waitKey(0)
