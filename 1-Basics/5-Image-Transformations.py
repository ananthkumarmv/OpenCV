import numpy as np
import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park', img)



# 1. Translation
def translate(img, x, y):        # x and y represent the number of pixels we wanted to shift along x and y axis
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[0], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)



# -x --> Left
# +x --> Right
# -y --> Up
# +y --> Down


translated = translate(img, 100, 100)
cv.imshow('Translated ++', translated)


# 2. Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)



# 3. Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)



# 4.Flipping 

# 0 --> flips over x axis or vertical flip
flip = cv.flip(img, 0)      
cv.imshow('Flip 0', flip)

# 1 --> flips over y axis or horizontal flip
flip = cv.flip(img, 1)
cv.imshow('Flip 1', flip)


# -1 --> flips over x axis as well as y axis or flip over both axis
flip = cv.flip(img, -1)
cv.imshow('Flip -1', flip)


# 5. Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
