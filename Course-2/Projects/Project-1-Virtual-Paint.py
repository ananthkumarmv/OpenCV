import cv2 as cv
import numpy as np


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



def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        # Getting the area of detected contour
        area = cv.contourArea(cnt)
        if area>500:
            #cv.drawContours(imgResult, cnt, -1, (255, 0, 0), thickness=3)
            # Getting the perimeter of the shape
            peri = cv.arcLength(cnt, True)

            # Getting the number of corners of the shape
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)

            x, y, w, h = cv.boundingRect(approx)

    return x+w//2, y+h//2



# List of colors to detect
# pink and yellow
myColors = [[168, 179, 130, 240, 150, 225],
            [26, 78, 93, 237, 60, 255]]

colors = [[106, 51, 170],
          [0, 255, 255]]

myPoints = []  # [x_, y_, colorId]



def findColor(img, myColors, colors):

    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    for i in range(len(myColors)):
        lower = np.array((myColors[i][0], myColors[i][2], myColors[i][4]))
        upper = np.array((myColors[i][1], myColors[i][3], myColors[i][5]))

        mask = cv.inRange(imgHSV, lower, upper)

        x, y = getContours(mask)
        cv.circle(imgResult, (x, y), 10, colors[count], -1)
        count += 1



# Web cam
cap = cv.VideoCapture(1)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)


while True:
    success, img = cap.read()

    imgResult = img.copy()

    findColor(img, myColors, colors)

    cv.imshow('Result', imgResult)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break




######################  Color Picker code  ###################



# # Trackbar Window
# def empty(a):
#     pass

# cv.namedWindow('TrackBars')
# cv.resizeWindow('TrackBars', 640, 240)
# cv.createTrackbar('Hue Minimum', 'TrackBars', 0, 179, empty)
# cv.createTrackbar('Hue Maximum', 'TrackBars', 0, 179, empty)
# cv.createTrackbar('Saturatioon Minimum', 'TrackBars', 0, 255, empty)
# cv.createTrackbar('Saturatioon Maximum', 'TrackBars', 0, 255, empty)
# cv.createTrackbar('Value Minimum', 'TrackBars', 0, 255, empty)
# cv.createTrackbar('Value Maximum', 'TrackBars', 0, 255, empty)



# while True:
#     success, img = cap.read()

#     hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    
#     h_min = cv.getTrackbarPos('Hue Minimum', "TrackBars")
#     h_max = cv.getTrackbarPos('Hue Maximum', "TrackBars")
#     s_min = cv.getTrackbarPos('Saturatioon Minimum', "TrackBars")
#     s_max = cv.getTrackbarPos('Saturatioon Maximum', "TrackBars")
#     v_min = cv.getTrackbarPos('Value Minimum', "TrackBars")
#     v_max = cv.getTrackbarPos('Value Maximum', "TrackBars")


#     # print(h_min, h_max, s_min, s_max, v_min, v_max)

#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])

#     mask = cv.inRange(hsvImg, lower, upper)

#     imgResult = cv.bitwise_and(img, img, mask=mask)

#     imgStack = stackImages(0.6, ([img, mask, imgResult]))

#     cv.imshow('Stacked Images', imgStack)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break



cv.waitKey(0)
