#!/usr/bin/env python3
import os
import time
import serial
from tkinter import *
from PIL import Image, ImageTk

class App():
    def __init__(self):
        #create bluetooh object
        self.ser = serialInterface()
        #create root gui
        self.root = Tk()
        self.root.title("INTERFACE by NZURU")
        self.root.config(bg="white")
        self.root.resizable(0,0)
        #create frame
        self.myframe = Frame()
        self.myframe.pack(fill="both",expand="True")
        #change color de frame
        self.myframe.config(bg="white")
        self.myframe.config(width="650",height="500")
        self.myframe.config(bd=35)
        self.myframe.config(relief="groove")
        self.myframe.config(cursor="hand2")

        self.zero_frame = Frame(self.myframe, bg="white")
        self.zero_frame.grid(row=0, column=0)

        self.first_frame = Frame(self.myframe, bg="white")
        self.first_frame.grid(row=1, column=0)
        
        self.second_frame = Frame(self.myframe, bg="white")
        self.second_frame.grid(row=2, column=0)

        self.third_frame = Frame(self.myframe, bg="white")
        self.third_frame.grid(row=3, column=0)

        self.four_frame = Frame(self.myframe, bg="white")
        self.four_frame.grid(row=4, column=0)

        #self.sensorString1 = StringVar()
        self.sensorString1 = StringVar()
        self.sensorString2 = StringVar()
        self.sensorString3 = StringVar()
        self.sentString = StringVar()

        self.b1 = IntVar()
        self.b2 = IntVar()
        self.b3 = IntVar()
        self.b4 = IntVar()
        self.b5 = IntVar()
        self.controlType = IntVar()

        self.B1 = Checkbutton(self.first_frame,text="Button1",fg="red",variable=self.b1)  
        self.B1.grid(row=2,column=1,sticky="e",padx=50,pady=20)

        self.B2 = Checkbutton(self.first_frame,text="Button2",fg="red",variable=self.b2)  
        self.B2.grid(row=2,column=2,sticky="e",padx=50,pady=20)

        self.B3 = Checkbutton(self.first_frame,text="Button3",fg="red",variable=self.b3) 
        self.B3.grid(row=2,column=3,sticky="e",padx=50,pady=20)

        self.B4 = Checkbutton(self.first_frame,text="Button4",fg="red",variable=self.b4)  
        self.B4.grid(row=2,column=4,sticky="e",padx=50,pady=20)

        self.B5 = Checkbutton(self.first_frame,text="Button5",fg="red",variable=self.b5)  
        self.B5.grid(row=2,column=5,sticky="e",padx=50,pady=20)

        self.CONTROL = Checkbutton(self.second_frame,text="Remote Control",fg="red",variable=self.controlType)  
        self.CONTROL.grid(row=0,column=0,sticky="e",padx=50,pady=40)

        self.led1 = 0
        self.led2 = 0
        self.led3 = 0 
        self.led4 = 0
        self.led5 = 0
        
        self.on = Image.open('off.png')
        self.ON = ImageTk.PhotoImage(self.on)

        self.off = Image.open('on.png')
        self.OFF = ImageTk.PhotoImage(self.off)

        self.logo = Image.open('NZURU.png')
        self.LOGO = ImageTk.PhotoImage(self.logo)

        self.LOG_V = Label(self.zero_frame,image=self.LOGO)
        self.LOG_V.grid(row=0,column=3,padx=50,pady=20)

        self.LED1 = Label(self.first_frame, image=self.OFF)
        self.LED1.grid(row=1,column=1,padx=50,pady=20)

        self.LED2 = Label(self.first_frame, image=self.OFF)
        self.LED2.grid(row=1,column=2,padx=50,pady=20)

        self.LED3 = Label(self.first_frame, image=self.OFF)
        self.LED3.grid(row=1,column=3,padx=50,pady=20)

        self.LED4 = Label(self.first_frame, image=self.OFF)
        self.LED4.grid(row=1,column=4,padx=50,pady=20)

        self.LED5 = Label(self.first_frame, image=self.OFF)
        self.LED5.grid(row=1,column=5,padx=50,pady=20)

        self.labelVoltage = Label(self.third_frame, text="Voltage(V)")
        self.labelVoltage.grid(row=0,column=0,padx=5,pady=5)
        self.labelVoltage.config(fg="red",justify="center")
        self.labelVoltage.config(bd=10)
        self.labelVoltage.config(relief="groove")

        self.labelTemperature = Label(self.third_frame , text="Temperature(°C)")
        self.labelTemperature.grid(row=0,column=2,padx=50,pady=10)
        self.labelTemperature.config(fg="red",justify="center")
        self.labelTemperature.config(bd=10)
        self.labelTemperature.config(relief="groove")

        self.labelRH = Label(self.third_frame, text="Relative Humidity(%)")
        self.labelRH.grid(row=0,column=4,padx=50,pady=10)
        self.labelRH.config(fg="red",justify="center")
        self.labelRH.config(bd=10)
        self.labelRH.config(relief="groove")

        self.labelSensor1 = Entry(self.third_frame,textvariable=self.sensorString1, bg="white")
        self.labelSensor1.grid(row=1,column=0,padx=50,pady=10)
        self.labelSensor1.config(fg="red",justify="center")
        self.labelSensor1.config(bd=10)
        self.labelSensor1.config(relief="groove")
        
        self.labelSensor2 = Entry(self.third_frame,textvariable=self.sensorString2, bg="white")
        self.labelSensor2.grid(row=1,column=2,padx=50,pady=10)
        self.labelSensor2.config(fg="red",justify="center")
        self.labelSensor2.config(bd=10)
        self.labelSensor2.config(relief="groove")

        self.labelSensor3 = Entry(self.third_frame ,textvariable=self.sensorString3, bg="white")
        self.labelSensor3.grid(row=1,column=4,padx=50,pady=10)
        self.labelSensor3.config(fg="red",justify="center")
        self.labelSensor3.config(bd=10)
        self.labelSensor3.config(relief="groove")

        self.labelSend = Label(self.four_frame, text="Write a message: ")
        self.labelSend.grid(row=0,column=0,padx=10,pady=40)
        self.labelSend.config(fg="red",justify="center")
        self.labelSend.config(bd=10)
        self.labelSend.config(relief="groove")

        self.labelSent = Entry(self.four_frame,textvariable=self.sentString,bg="white")
        self.labelSent.grid(row=0,column=1,padx=10,pady=40)
        self.labelSent.config(fg="red",justify="center")
        self.labelSent.config(bd=10)
        self.labelSent.config(relief="groove")

        self.root.after(3,self.connect_push)
        self.root.mainloop()

    def close(self):
        self.ser.close_Serial()

    def connect_push(self):
        while True: 
            data = self.ser.data_read()
            if self.controlType.get():
                self.led1 = int(self.b1.get())
                self.led2 = int(self.b2.get())
                self.led3 = int(self.b3.get())
                self.led4 = int(self.b4.get())
                self.led5 = int(self.b5.get())
                if self.led1:
                    self.LED1.configure(image=self.ON)
                else:
                    self.LED1.configure(image=self.OFF)

                if self.led2:
                    self.LED2.configure(image=self.ON)
                else:
                    self.LED2.configure(image=self.OFF)
                
                if self.led3:
                    self.LED3.configure(image=self.ON)
                else:
                    self.LED3.configure(image=self.OFF)
                if self.led4:
                    self.LED4.configure(image=self.ON)
                else:
                    self.LED4.configure(image=self.OFF)

                if self.led5:
                    self.LED5.configure(image=self.ON)
                else:
                    self.LED5.configure(image=self.OFF)
            
            else:
                
                self.led1 = int(data[0])
                self.led2 = int(data[1])
                self.led3 = int(data[2])
                self.led4 = int(data[3])
                self.led5 = int(data[4])

                if self.led1:
                    self.LED1.configure(image=self.ON)
                else:
                    self.LED1.configure(image=self.OFF)

                if self.led2:
                    self.LED2.configure(image=self.ON)
                else:
                    self.LED2.configure(image=self.OFF)
                
                if self.led3:
                    self.LED3.configure(image=self.ON)
                else:
                    self.LED3.configure(image=self.OFF)

                if self.led4:
                    self.LED4.configure(image=self.ON)
                else:
                    self.LED4.configure(image=self.OFF)

                if self.led5:
                    self.LED5.configure(image=self.ON)
                else:
                    self.LED5.configure(image=self.OFF)
            self.sensorString1.set(data[5])
            self.sensorString2.set(data[6])
            self.sensorString3.set(data[7])
            s = self.sentString.get()
            data = "\t{}{}{}{}{}{}\n{}".format(int(self.controlType.get()),self.led1,self.led2,self.led3,self.led4,self.led5,s)
            self.ser.send_data(data)
            self.root.update()

class serialInterface():
    def __init__(self):
        self.encoding = 'Ascii' 
        self.port = '/dev/ttyUSB0'
        self.bauds = 115200
        self.picSerial = serial.Serial(self.port,self.bauds)
        time.sleep(2)

    def data_read(self):
        data = self.picSerial.readline()
        data_str = data.decode(self.encoding)
        data_sensors = self.get_values(data_str) 
        data_split = data_sensors.split(',')
        data_int = []
        for value in data_split:
             data_int.append(float(value))
        return  data_int 

    def send_data(self,data):
        data = data.encode()
        self.picSerial.write(data)

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
    def close_Serial(self):
        self.picSerial.close()
        self.picSerial.close()

if __name__=='__main__':
    app = App()
    app.close()
    os.system ("clear") 