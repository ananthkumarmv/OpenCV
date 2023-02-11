import cv2 as cv

# Reading Images

# returns matrix of pixels
img = cv.imread('Resources/Photos/cat_large.jpg')
# displaying image
cv.imshow('Cat', img)
cv.waitKey(0)




# Reading Videos

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# reading the video frame-by-frame
while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):    # if the letter 'd' is pressed stop playing video
        break

capture.release()
cv.destroyAllWindows()

