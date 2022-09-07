import cv2
import numpy as np

cap = cv2.VideoCapture('000.avi')

#ret,frame1 = cap.read()  # Capturing the first and second frame
#ret,frame2 = cap.read()

while cap.isOpened():
     if ret == False:
         break
     diff = cv2.absdiff(frame1,frame2)
     gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
     blur = cv2.GaussianBlur(gray, (15,15),0)
     _,thresh = cv2.threshold(blur,20,255,0)
     dilate = cv2.dilate(thresh,None,iterations = 10)


     contours,hierarchy = cv2.findContours(dilate,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

     #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
     for contour in contours:
         (x,y,w,h) = cv2.boundingRect(contour)
         if cv2.contourArea(contour)>2000 :
             cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255 , 0), 2)
     cv2.imshow("video",frame1)
     frame1 = frame2
     ret,frame2 = cap.read()

     k = cv2.waitKey(200)
     if k == 27:
        break

    ret, frame=cap.read()
    cv2.imshow("inter",frame)
    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()