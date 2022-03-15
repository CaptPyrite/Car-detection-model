import cv2
import numpy as np

cap = cv2.VideoCapture('car.jpg')#car.jpl

font = cv2.FONT_HERSHEY_TRIPLEX

harcascade = cv2.CascadeClassifier("cars.xml")

while True:
    ret,frames = cap.read()
    
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    
    cars = harcascade.detectMultiScale(gray, 5, 2)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frames,str("Car"),(x,y+h),font,1,255)
     
    
    cv2.imshow('img',frames)   

     
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
    
cap.release()
cv2.destroyAllWindows()