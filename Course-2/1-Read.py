import cv2 as cv


# ########################## Read Image ############################
# Loading an image using 'imread'
img = cv.imread('Resources/lena.png')


# Displaying an Image using 'imshow'
cv.imshow('Output', img)  # (name_of_the_window, img_matrix)


########################## Read Video ############################

cap = cv.VideoCapture('Resources/test_video.mp4')

while True:
    # img - image matrix is stored -- since video is a sequence of images.
    # success variable tells us whether its done successfully or not(its value will be 'True' or 'False').
    success, img = cap.read()

    cv.imshow('Video', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.waitKey(0)



########################## Read Web Cam #########################

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv.imshow('Web Cam Live', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.waitKey(0)          # delay in milisecond; (0) means infinite delay