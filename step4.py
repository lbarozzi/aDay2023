#!/bin/env python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


#Haar
haar_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')


cnt=0
sens=8
while True:
    cnt+=1
    if cnt%sens==0:
        success, img = cap.read()

        grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(grayscale)
        
        
        faces_rect=haar_cascade.detectMultiScale(grayscale,scaleFactor=1.25, minNeighbors=3,minSize=(30,30))
        
        for (x,y,w,h) in faces_rect:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=1)
            #Crop Area
            face_img=grayscale[y:y+h,x:x+w]
            face_col=img[y:y+x,x:x+w]

        cv2.imshow('detected faces',img)
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

