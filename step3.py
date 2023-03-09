#!/bin/env python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


cnt=0
sens=8
while True:
    cnt+=1
    
    if cnt%sens==0:
        success, img = cap.read()
    
    
        grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(grayscale)
        
      
        cv2.imshow('detected faces',img)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

