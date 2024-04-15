import cv2 as cv
import sys

img_link= cv.samples.findFile("dog.jpg")
img = cv.imread(img_link, cv.IMREAD_GRAYSCALE ) #COLOR, UNCHANGED, GRAYSCALE
 
if img is None:
 sys.exit("Could not read the image.")
 
cv.imshow("Display window", img)
k = cv.waitKey(0)                       #if arg=0, wait until press. ortherwise wait amount of time. 
 
if k == ord("s"):       #ord() returns number representing it in unicode. 
 cv.imwrite("dog.png", img)
