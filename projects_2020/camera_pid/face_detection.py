#!/usr/bin/env python3
# import the opencv library 
import cv2 
import serial    
import time
class serialInterface():
    def __init__(self):
        self.encoding = 'Ascii' 
        self.port = '/dev/ttyUSB0'
        self.bauds = 115200
        self.picSerial = serial.Serial(self.port,self.bauds)
        time.sleep(2)

    def send_data(self,data):
        data = data.encode()
        self.picSerial.write(data)


    def close_Serial(self):
        self.picSerial.close()
        self.picSerial.close()


# define a video capture object 
vid = cv2.VideoCapture(2) 
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
data = ''  
serial = serialInterface()

while(True): 

    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceClassif.detectMultiScale(gray,scaleFactor = 1.3, minNeighbors = 5, minSize=(60,60), maxSize = (300,300))
    #serial.data_read()
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),5)   
        cv2.line(frame,(x+int(w/2),0),(x+int(w/2),int(frame.shape[0])),(255,0,0),2)
        cv2.line(frame,(0,y+int(h/2)),(int(frame.shape[1]),y+int(h/2)),(255,0,0),2)
        cv2.circle(frame,(x+int(w/2),y+int(h/2)), 5, (0,0,255),10)     
        positionText = "("+str(x+int(w/2))+","+str(y+int(h/2))+")"
        cv2.putText(frame,positionText, (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255))
        data = "{}\n".format(int(x+(w/2)))
        cv2.line(frame,(int(frame.shape[1]/2),0),(int(frame.shape[1]/2),int(frame.shape[0])),(0,0,255),4)
        #print(frame.shape[1]/2)  
    serial.send_data(data)        
    cv2.imshow('frame',frame)
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
serial.close_Serial()