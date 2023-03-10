import cv2 as cv
import numpy as np

path = 'Resources/lambo.png'
img = cv.imread(path)
# cv.imshow('Original', img)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver




def empty(a):
    pass

cv.namedWindow('TrackBars')
cv.resizeWindow('TrackBars', 640, 240)
cv.createTrackbar('Hue Minimum', 'TrackBars', 0, 179, empty)
cv.createTrackbar('Hue Maximum', 'TrackBars', 19, 179, empty)
cv.createTrackbar('Saturatioon Minimum', 'TrackBars', 111, 255, empty)
cv.createTrackbar('Saturatioon Maximum', 'TrackBars', 240, 255, empty)
cv.createTrackbar('Value Minimum', 'TrackBars', 153, 255, empty)
cv.createTrackbar('Value Maximum', 'TrackBars', 255, 255, empty)


imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', imgHSV)

while True:

    h_min = cv.getTrackbarPos('Hue Minimum', "TrackBars")
    h_max = cv.getTrackbarPos('Hue Maximum', "TrackBars")
    s_min = cv.getTrackbarPos('Saturatioon Minimum', "TrackBars")
    s_max = cv.getTrackbarPos('Saturatioon Maximum', "TrackBars")
    v_min = cv.getTrackbarPos('Value Minimum', "TrackBars")
    v_max = cv.getTrackbarPos('Value Maximum', "TrackBars")


    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(img, img, mask=mask)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))

    cv.imshow('Stacked Images', imgStack)

    cv.waitKey(1)


cv.waitKey(0)
