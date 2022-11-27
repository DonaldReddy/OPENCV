import cv2 as cv
import numpy as np

def func(self):
    pass

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("Hue Min","TrackBars",75,179,func)
cv.createTrackbar("Hue Max","TrackBars",179,179,func)
cv.createTrackbar("Sat Min","TrackBars",161,255,func)
cv.createTrackbar("Sat Max","TrackBars",255,255,func)
cv.createTrackbar("Val Min","TrackBars",0,255,func)
cv.createTrackbar("Val Max","TrackBars",255,255,func)

while True:
    img=cv.imread("flower.jpeg")
    img=cv.resize(img,(400,300))
    imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    hue_min=cv.getTrackbarPos("Hue Min","TrackBars")
    hue_max=cv.getTrackbarPos("Hue Max","TrackBars")
    sat_min=cv.getTrackbarPos("Sat Min","TrackBars")
    sat_max=cv.getTrackbarPos("Sat Max","TrackBars")
    val_min=cv.getTrackbarPos("Val Min","TrackBars")
    val_max=cv.getTrackbarPos("Val Max","TrackBars")
    print(hue_min,hue_max,sat_min,sat_max,val_min,val_max)
    lower=np.array([hue_min,sat_min,val_min])
    upper=np.array([hue_max,sat_max,val_max])
    mask=cv.inRange(imghsv,lower,upper)
    imgOut=cv.bitwise_and(img,img,mask=mask)

    cv.imshow("flower",img)
    cv.imshow("flower hsv",imghsv)
    cv.imshow("flower hsv mask",mask)
    cv.imshow("Result",imgOut)
    cv.waitKey(1)