import cv2 as cv
import numpy as np


img = cv.imread('Resources/lena.png')
cv.imshow('Original Image', img)

# 1. Gray Scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)


# 2. Blurring an Image
blur = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Blurred Image', blur)

# 3. Canny Image detector
canny = cv.Canny(img, 100, 100)
cv.imshow('Canny Edge Detector', canny)


kernel = np.ones((5, 5), np.uint8)

# 4. Image Dilation -- used to increased the thickness of edges detected by canny
dilated = cv.dilate(canny, kernel, iterations=1)
cv.imshow('Dilated Image', dilated)


# 5. Image eroding - opposite to dilation
erode = cv.erode(dilated, kernel, iterations=1)
cv.imshow('Eroded image', erode)




cv.waitKey(0)
