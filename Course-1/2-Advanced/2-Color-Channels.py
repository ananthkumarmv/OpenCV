import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)


# Splits the color channels
b, g, r = cv.split(img)

# Displays the respective colors in the form of grayscale -- the lighter intensity region represents the color presence.
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merging 
merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)




blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)