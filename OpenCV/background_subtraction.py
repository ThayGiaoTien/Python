import numpy as np
import cv2 as cv
import time
cap = cv.VideoCapture(0) #which camera.

while(1):
    _, frame= cap.read()

    if not _:
        print("Can't read the video")
    grayImage1= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('background', grayImage1)
    
    k= cv.waitKey(5)
    if k==ord('q'):
        break

while(1):
    _, frame1= cap.read()

    if not _:
        print("Can't read the video")
    grayImage2= cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    cv.imshow('foreground', grayImage2)
    
    difference= np.absolute(np.matrix(np.int16(grayImage2)-np.matrix(np.int16(grayImage1))))
    #clamp it
    difference[difference>255]=255
    print(np.matrix(difference), '\n')
    #display difference
    difference= np.uint8(difference)
    print(np.matrix(difference), '\n')
    cv.imshow('difference', difference)

    # Thesh Holding
    BW= difference
    AVR= np.sum(np.sum(BW))/(2*640*480) +20 #Assumming noise is less then 20
    print(AVR)
    # Be careful of the order  
    BW[BW<=AVR]=0
    BW[BW>AVR]= 1
    print(np.matrix(BW), '\n')

    #calculate the central mass of object
    col_sums= np.matrix(np.sum(BW,0))
    col_idx= np.matrix(np.arange(640))
    col_total= np.sum(np.multiply(col_sums, col_idx))
    total= np.sum(col_sums)+1
    col= col_total/total
    #print(col_total, '-' , total)

    row_sums= np.transpose(np.matrix((np.sum(BW,1))))
    row_idx= (np.arange(480))
    row_total= np.sum(np.multiply(row_sums, row_idx))
    row= row_total/total

    print('The position: ' , row, '-', col)
    
    time.sleep(1)
    k= cv.waitKey(5)
    if k==ord('q'):
        break
    
cv.destroyAllWindows()

print("Size of frame: ", frame.shape)
print(frame)
