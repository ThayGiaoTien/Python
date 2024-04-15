import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0) #which camera.

while(1):
    _, frame= cap.read()

    if not _:
        print("Can't read the video")

    blue_frame= frame[:,:, 0]
    green_frame = frame[:, :, 1]
    red_frame= frame[:,:, 2]
    cv.imshow('blue frame', blue_frame)
    cv.imshow('green frame', green_frame)
    cv.imshow('red frame', red_frame)
    cv.imshow('rgb frame', frame)

    k= cv.waitKey(5)
    if k==ord('q'):
        break
    
cv.destroyAllWindows()

print("Size of frame: ", frame.shape)
print(frame)
