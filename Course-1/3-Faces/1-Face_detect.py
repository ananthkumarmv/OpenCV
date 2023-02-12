import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Group of 5 people', img)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('3-Faces/haar_face.xml')

# returns face co-ordinates
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected faces', img)



cv.waitKey(0)
