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
    for cnt in contours:
        # Getting the area of detected contour
        area = cv.contourArea(cnt)
        print(area)
        if area>500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), thickness=3)
            # Getting the perimeter of the shape
            peri = cv.arcLength(cnt, True)
            print(peri)

            # Getting the number of corners of the shape
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            # '0' indicates 'Cirle' and '4' indicates 'Square'
            print(len(approx))

            objCor = len(approx)

            if objCor == 3:
                objType = 'Tri'
            elif objCor == 4:
                aspRatio = w/float(h)
                if(aspRatio >= 0.95 and aspRatio <= 1.03):
                    objType = 'Square'
                else:
                    objType = 'Rectangle'
            elif objCor > 4:
                objType = 'Circle'
            else:
                objType = 'None'

            x, y, w, h = cv.boundingRect(approx)


            # Printing bounding-box around detected shapes
            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0,255,0), 2)
            cv.putText(imgContour, objType, (x+w//2-10, y+h//2-10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2)



path = 'Resources/shapes.png'
img = cv.imread(path)
# cv.imshow('Original', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

blur = cv.GaussianBlur(gray, (7, 7), 1)
# cv.imshow("Blur Image", blur)

canny = cv.Canny(blur, 50, 50)

imgContour = img.copy()
getContours(canny)

blank = np.zeros_like(img)

imgStack = stackImages(0.6, ([img, gray, blur], 
                             [canny, imgContour, blank]))

cv.imshow('Stacked Images', imgStack)


cv.waitKey(0)
