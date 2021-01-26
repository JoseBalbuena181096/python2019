#!/usr/bin/env python3
import os
import time
import bluetooth
from tkinter import *

class App():
    def __init__(self):
        #create bluetooh object
        self.blu = bluetoothClient()
        #create root gui
        self.root = Tk()
        self.root.title("CAR AUTOMATION")
        self.root.config(bg="blue")
        #create frame
        self.myframe = Frame()
        self.myframe.pack(fill="both",expand="True")
        #change color de frame
        self.myframe.config(bg="blue")
        self.myframe.config(width="650",height="500")
        self.myframe.config(bd=35)
        self.myframe.config(relief="groove")
        self.myframe.config(cursor="hand2")

        self.sensorString1 = StringVar()
        self.sensorString2 = StringVar()
        self.sensorString3 = StringVar()

        self.sensor1 = Label(self.myframe,text="Sensor 1: ",fg="red",font=(30)) 
        self.sensor1.grid(row=0,column=0,sticky="e",padx=50,pady=20)
        self.sensor2 = Label(self.myframe,text="Sensor 2: ",fg="red",font=(30))
        self.sensor2.grid(row=1,column=0,sticky="e",padx=50,pady=20)
        self.sensor3 = Label(self.myframe,text="Sensor 3: ",fg="red",font=(30))
        self.sensor3.grid(row=2,column=0,sticky="e",padx=50,pady=20)

        self.labelSensor1 = Entry(self.myframe,textvariable=self.sensorString1)
        self.labelSensor1.grid(row=0,column=1,padx=5,pady=5)
        self.labelSensor1.config(fg="red",justify="right")
        self.labelSensor2 = Entry(self.myframe,textvariable=self.sensorString2)
        self.labelSensor2.grid(row=1,column=1,padx=5,pady=5)
        self.labelSensor2.config(fg="red",justify="right")
        self.labelSensor3 = Entry(self.myframe,textvariable=self.sensorString3)
        self.labelSensor3.grid(row=2,column=1,padx=5,pady=5)
        self.labelSensor3.config(fg="red",justify="right")
        self.disconnetButton=Button(self.myframe,text="EXIT",command = self.disconnect_push)
        self.disconnetButton.grid(row=3,column=1,padx=10,pady=10)
        self.root.after(3,self.connect_push)
        self.root.mainloop()
    def connect_push(self):
        try:
            while 1:
                data = []
                data = self.blu.get_data()
                if len(data) == 3:
                    #print(data)
                    self.blu.send_data("b") # Echo back to client
                    self.sensorString1.set(data[0])
                    self.sensorString2.set(data[1])
                    self.sensorString3.set(data[2])
                self.root.update()
        except:	
            self.blu.send_data("a")
            #print("Closing socket")
            self.blu.send_data("b")
            self.blu.close_bluetooth()
    def disconnect_push(self):
            self.root.destroy()
            self.blu.send_data("a")
            time.sleep(1)
            #print("Closing socket")
            self.blu.close_bluetooth()
    def __del__(self):
            self.root.destroy()
            self.blu.send_data("a")
            time.sleep(1)
            #print("Closing socket")
            self.blu.close_bluetooth()
class bluetoothClient():
    def __init__(self):
        self.encoding = 'utf-8' 
        self.address = '00:18:E5:04:8E:19'
        self.port = 1
        self.client = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.client.connect((self.address,self.port))
    def get_data(self):
        data = self.client.recv(4096)
        time.sleep(1)
        data_str = data.decode(self.encoding)
        data_sensors = self.get_values(data_str) 
        data_split = data_sensors.split(',')
        return data_split

    def send_data(self,data):
        self.client.send(data) 
    def find_character(self,data,character):
        index = 0
        while index < len(data):
            if data[index] == character:
                return index
            index += 1
        return -1

    def get_values(self,data):
        j = self.find_character(data,"\t")
        if j != -1:
            w = self.find_character(data[j+1:],"\n")
        return data[j+1:w+1]
    def close_bluetooth(self):
        self.client.close()

if __name__=='__main__':
    app = App()