import cv2 as cv
import numpy as np



blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)


# 2. painting the image a certain color
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red', blank)





# 3. Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0,255,0), thickness=2)  # cv.rectangle(img, startingPoint, endingPoint, colorOfRectangle, thicknessOfRectangle)
cv.imshow("Rectangle", blank)

# 4. Draw a rectangle and fill
cv.rectangle(blank, (0, 0), (250, 250), (255,0,0), thickness=-1)  # '-1' can be replaced with cv.FILLED
cv.imshow("Rectangle Filled with blue", blank)


# 4. Draw a rectangle and fill
cv.rectangle(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (255,0,0), thickness=cv.FILLED)  # cv.FILLED can be replaced with '-1'
cv.imshow("Same as Above", blank)






# 5. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow("Circle", blank)







# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow("Line", blank)





# Writing a text on image
cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)



cv.waitKey(0)

