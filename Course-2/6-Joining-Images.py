import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/anant/OneDrive/Documents/GitHub/OpenCV/Course-2/Resources/lena.png')

# Joining Horizontally
imgHor = np.hstack((img, img))
cv.imshow('Horizontal', imgHor)


# Joining Vertically
imgVer = np.vstack((img, img))
cv.imshow('Vetical', imgVer)

cv.waitKey(0)
