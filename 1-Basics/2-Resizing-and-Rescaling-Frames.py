import cv2 as cv


# Resizing function
# This method works for Images, pre-captured videos and Live Videos
def rescaleFrame(frame, scale=0.75):

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)





# This method works only for Live video not for videos already exist
def changeResolution(width, height):

    capture.set(3, width)
    capture.set(4, height)




# Displaying the large image

img = cv.imread('Resources/Photos/cat_large.jpg')
# displaying image
cv.imshow('Cat', img)


# Displaying the resized image
resized_image = rescaleFrame(img)
cv.imshow('Resized Cat Image', resized_image)
# cv.waitKey(0)







# Displaying the Video

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# reading the video frame-by-frame
while True:
    isTrue, frame = capture.read()

    # Displaying the rescaled frame
    frame_resized = rescaleFrame(frame, scale=0.2)
    
    # Displaying the original frame
    cv.imshow('Video', frame)

    
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):    # if the letter 'd' is pressed stop playing video
        break

capture.release()
cv.destroyAllWindows()
