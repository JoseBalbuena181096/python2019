
#!/usr/bin/env python3
from tkinter import *
root = Tk()

def connect_push():
    sensorString1.set("push connect")
def disconnect_push():
    sensorString2.set("push disconnect")

root.title("CAR AUTOMATION")
#root.resizable(1,1)
root.config(bg="blue")
#create frame
myframe = Frame()
#package frame
myframe.pack(fill="both",expand="True")
#change color de frame
myframe.config(bg="blue")
myframe.config(width="650",height="500")
myframe.config(bd=35)
myframe.config(relief="groove")
myframe.config(cursor="hand2")

sensorString1 = StringVar()
sensorString2 = StringVar()
sensorString3 = StringVar()

sensor1 = Label(myframe,text="Sensor 1: ",fg="red",font=(30)) 
sensor1.grid(row=0,column=0,sticky="e",padx=50,pady=20)
sensor2 = Label(myframe,text="Sensor 2: ",fg="red",font=(30))
sensor2.grid(row=1,column=0,sticky="e",padx=50,pady=20)
sensor3 = Label(myframe,text="Sensor 3: ",fg="red",font=(30))
sensor3.grid(row=2,column=0,sticky="e",padx=50,pady=20)

labelSensor1 = Entry(myframe,textvariable=sensorString1)
labelSensor1.grid(row=0,column=1,padx=5,pady=5)
labelSensor1.config(fg="red",justify="right")
labelSensor2 = Entry(myframe,textvariable=sensorString2)
labelSensor2.grid(row=1,column=1,padx=5,pady=5)
labelSensor2.config(fg="red",justify="right")
labelSensor3 = Entry(myframe,textvariable=sensorString3)
labelSensor3.grid(row=2,column=1,padx=5,pady=5)
labelSensor3.config(fg="red",justify="right")


connetButton=Button(myframe,text="Connect",command=connect_push)
connetButton.grid(row=3,column=0,padx=10,pady=10)
disconnetButton=Button(myframe,text="Disconnect",command=disconnect_push)
disconnetButton.grid(row=3,column=1,padx=10,pady=10)

root.mainloop()
