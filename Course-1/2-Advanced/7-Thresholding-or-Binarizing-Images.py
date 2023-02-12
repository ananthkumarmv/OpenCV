import cv2 as cv


img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 1. Simple thresholding

# Setting pixels values which are greather than 150 ---> 255
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded 100', thresh)


# Setting pixels values which are less than 150 ---> 255
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded', thresh_inv)


# 2. Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)


cv.waitKey(0)
