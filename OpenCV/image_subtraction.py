import numpy as np
import cv2 as cv
import time
cap = cv.VideoCapture(0) #which camera.

while(1):
    _, frame= cap.read()

    if not _:
        print("Can't read the video")

    blue= np.matrix(frame[:,:, 0])
    green = np.matrix(frame[:, :, 1])
    red= np.matrix(frame[:,:, 2])
    #cv.imshow('blue frame', blue_frame)
    #cv.imshow('green frame', green_frame)
    #cv.imshow('red frame', red_frame)
    #cv.imshow('rgb frame', frame)

    # To calculate signed value, we have to convert from uint8 to int16
    # Then clamp it and convert back to uint8
    red_only= np.int16(red)-np.int16(green)
    red_only[red_only>=255] = 255
    red_only[red_only<=0]= 0

    red_only= np.uint8(red_only)

    # Algorithm to find the center mass of an object.(in this case: red object)
    # The resolution= the matrix size= 640x480
    col_sums= np.sum(red_only, 0)
    col_indexes = np.matrix(np.arange(640))
    col_total = np.sum(np.multiply(col_sums,col_indexes))

    row_sums= np.sum(red_only, 1)
    row_indexes = np.transpose(np.matrix(np.arange(480)))
    row_total = np.sum(np.multiply(row_sums,row_indexes))

    total = np.sum(col_sums)
    central_col = col_total/total
    central_row= row_total/total
    
    print('row-col: ', central_row, '-',central_col)
    time.sleep(2)
    
    cv.imshow('red_only', np.uint8(red_only))

    k= cv.waitKey(5)
    if k==ord('q'):
        break
    
cv.destroyAllWindows()

print("Size of frame: ", frame.shape)
print(frame)
