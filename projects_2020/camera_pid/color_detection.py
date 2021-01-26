#!/usr/bin/env python3
# import the opencv library 
import cv2 
import numpy as np    
# define a video capture object 
vid = cv2.VideoCapture(2) 
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

while(True): 

    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    """
    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),5)   
    cv2.line(frame,(x+int(w/2),0),(x+int(w/2),int(frame.shape[0])),(255,0,0),2)
    cv2.line(frame,(0,y+int(h/2)),(int(frame.shape[1]),y+int(h/2)),(255,0,0),2)
    cv2.circle(frame,(x+int(w/2),y+int(h/2)), 5, (0,0,255),10)
    positionText = "("+str(x+int(w/2))+","+str(y+int(h/2))+")"
    cv2.putText(frame,positionText, (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255))
    """
    low_red = np.array([94,80,2])
    high_red = np.array([126,255,255])
    red_mask = cv2.inRange(frame,low_red,high_red)
    red = cv2.bitwise_and(frame,frame,mask=red_mask)
    cv2.imshow('frame',red)
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 