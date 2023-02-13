import cv2 as cv
import numpy as np


img = cv.imread('Resources/cards.jpg')
cv.imshow('Image', img)


cv.waitKey(0)