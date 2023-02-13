import cv2 as cv
import numpy as np


img = cv.imread('Resources/lambo.png')
cv.imshow('Original Image', img)

print(img.shape)

# 1. Resizing an image
resizedImg = cv.resize(img, (300, 200))
cv.imshow('Resized Image', resizedImg)

# 2. Cropping an image -- [height, width]
croppedImg = img[100:-50, 30:-80]
cv.imshow('Cropped Image', croppedImg)

cv.waitKey(0)
