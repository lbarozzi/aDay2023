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
#haar_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_alt_tree.xml')
haar_cascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_righteye_2splits.xml')
smile_cascade = cv2.CascadeClassifier('Resources/haarcascades/haarcascade_smile.xml')

cnt=0
sens=8
while True:
    success, img = cap.read()

    grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.equalizeHist(grayscale)
    
    if cnt%sens==0:
        faces_rect=haar_cascade.detectMultiScale(grayscale,scaleFactor=1.25, minNeighbors=3,minSize=(30,30))
    
    for (x,y,w,h) in faces_rect:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=1)
        cv2.rectangle(img,(x,y),(x+w,y+h+30),(0,255,0),thickness=1)
        cv2.putText(img,"Face",(x,y+h+30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),1)

        #Crop Area
        face_img=grayscale[y:y+h,x:x+w]
        face_col=img[y:y+x,x:x+w]

        #Search for eyes and mounth
        smiles= smile_cascade.detectMultiScale(face_img,scaleFactor=1.3,minNeighbors=5,minSize=(50,20))
        eyes= eye_cascade.detectMultiScale(face_img,scaleFactor=1.25)

        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(face_col,(sx,sy),(sx+sw,sy+sw),(128,128,128),2)

        for (x,y,w,h) in eyes:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),thickness=1)

  
    cv2.imshow('detected faces',img)
    
    cnt+=1
#    cv2.waitKey()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

