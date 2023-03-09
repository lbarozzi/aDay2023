#!/bin/env python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


success, img = cap.read()
  
cv2.imshow('detected faces',img)
    

cv2.waitKey(-1)

cv2.destroyAllWindows()
