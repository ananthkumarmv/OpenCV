import cv2 as cv


path = 'C:/Users/anant/OneDrive/Documents/GitHub/OpenCV/Course-2/Resources/lambo.png'
img = cv.imread(path)
cv.imshow('Original', img)


imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', imgHSV)


cv.waitKey(0)
