#!/usr/bin/env python3
import os
import time
import serial
from tkinter import *
from PIL import Image, ImageTk

class App():
    def __init__(self):
        #create bluetooh object
        #self.ser = serialInterface()
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

        self.fourth_frame = Frame(self.myframe, bg="white")
        self.fourth_frame.grid(row=4, column=0)

        self.fifth_frame = Frame(self.myframe, bg="white")
        self.fifth_frame.grid(row=5, column=0)

        self.sixth_frame = Frame(self.myframe, bg="white")
        self.sixth_frame.grid(row=6, column=0)

        #self.sensorString1 = StringVar()
        self.FULL_BOX_String = StringVar()
        self.EMPTY_BOX_String = StringVar()
        self.BOX_ENTRY_String = StringVar()
        self.BOX_EXIT_String = StringVar()

        self.b1 = IntVar()
        self.b2 = IntVar()
        self.b3 = IntVar()
        self.b4 = IntVar()
        self.b5 = IntVar()
        self.b6 = IntVar()
        self.b7 = IntVar()
        self.b8 = IntVar()
        self.b9 = IntVar()


        self.led1 = 0
        self.led2 = 0
        self.led3 = 0 
        self.led4 = 0
        self.led5 = 0
        
        self.on = Image.open("/home/jose/Desktop/jesus/on.jpg")
        self.ON = ImageTk.PhotoImage(self.on)

        self.off = Image.open("/home/jose/Desktop/jesus/off.jpg")
        self.OFF = ImageTk.PhotoImage(self.off)

        self.logo = Image.open("/home/jose/Desktop/jesus/rack.jpg")
        self.LOGO = ImageTk.PhotoImage(self.logo)
        
        self.a_image = Image.open("/home/jose/Desktop/jesus/a.jpg")
        self.A_IMAGE = ImageTk.PhotoImage(self.a_image)

        self.b_image = Image.open("/home/jose/Desktop/jesus/b.jpg")
        self.B_IMAGE = ImageTk.PhotoImage(self.b_image)

        self.c1_image = Image.open("/home/jose/Desktop/jesus/c1.jpg")
        self.C1_IMAGE = ImageTk.PhotoImage(self.c1_image)

        self.c2_image = Image.open("/home/jose/Desktop/jesus/c2.jpg")
        self.C2_IMAGE = ImageTk.PhotoImage(self.c2_image)

        self.c3_image = Image.open("/home/jose/Desktop/jesus/c3.jpg")
        self.C3_IMAGE = ImageTk.PhotoImage(self.c3_image)

        self.c4_image = Image.open("/home/jose/Desktop/jesus/c4.jpg")
        self.C4_IMAGE = ImageTk.PhotoImage(self.c4_image)

        self.LOG_V = Label(self.zero_frame,image=self.LOGO)
        self.LOG_V.grid(row=0,column=3,padx=50,pady=10)

        self.BOX1 = Label(self.first_frame, image=self.OFF)
        self.BOX1.grid(row=1,column=1,padx=50,pady=10)

        self.BOX2 = Label(self.first_frame, image=self.OFF)
        self.BOX2.grid(row=1,column=2,padx=50,pady=10)
        
        self.BOX3 = Label(self.first_frame, image=self.OFF)
        self.BOX3.grid(row=1,column=3,padx=50,pady=10)

        self.BOX4 = Label(self.first_frame, image=self.OFF)
        self.BOX4.grid(row=2,column=1,padx=50,pady=10)

        self.BOX5 = Label(self.first_frame, image=self.OFF)
        self.BOX5.grid(row=2,column=2,padx=50,pady=10)

        self.BOX6 = Label(self.first_frame, image=self.OFF)
        self.BOX6.grid(row=2,column=3,padx=50,pady=10)

        self.BOX7 = Label(self.first_frame, image=self.OFF)
        self.BOX7.grid(row=3,column=1,padx=50,pady=10)

        self.BOX8 = Label(self.first_frame, image=self.OFF)
        self.BOX8.grid(row=3,column=2,padx=50,pady=10)

        self.BOX9 = Label(self.first_frame, image=self.OFF)
        self.BOX9.grid(row=3,column=3,padx=50,pady=10)

        self.A_IMAGE_V = Label(self.second_frame,image=self.A_IMAGE)
        self.A_IMAGE_V.grid(row=1,column=3,padx=50,pady=20)

        self.B1 = Checkbutton(self.third_frame,text="Caja1",fg="black",variable=self.b1)  
        self.B1.grid(row=1,column=1,sticky="e",padx=50,pady=20)

        self.B2 = Checkbutton(self.third_frame,text="Caja2",fg="black",variable=self.b2)  
        self.B2.grid(row=1,column=2,sticky="e",padx=50,pady=20)

        self.B3 = Checkbutton(self.third_frame,text="Caja3",fg="black",variable=self.b3) 
        self.B3.grid(row=1,column=3,sticky="e",padx=50,pady=20)

        self.B4 = Checkbutton(self.third_frame,text="Caja4",fg="black",variable=self.b4)  
        self.B4.grid(row=1,column=4,sticky="e",padx=50,pady=20)

        self.B5 = Checkbutton(self.third_frame,text="Caja5",fg="black",variable=self.b5)  
        self.B5.grid(row=1,column=5,sticky="e",padx=50,pady=20)

        self.B6 = Checkbutton(self.fourth_frame,text="Caja6",fg="black",variable=self.b6)  
        self.B6.grid(row=1,column=1,sticky="e",padx=50,pady=20)

        self.B7 = Checkbutton(self.fourth_frame,text="Caja7",fg="black",variable=self.b7)  
        self.B7.grid(row=1,column=2,sticky="e",padx=50,pady=20)

        self.B8 = Checkbutton(self.fourth_frame,text="Caja8",fg="black",variable=self.b8) 
        self.B8.grid(row=1,column=3,sticky="e",padx=50,pady=20)

        self.B9 = Checkbutton(self.fourth_frame,text="Caja9",fg="black",variable=self.b9)  
        self.B9.grid(row=1,column=4,sticky="e",padx=50,pady=20)

        self.B_IMAGE_V = Label(self.fifth_frame,image=self.B_IMAGE)
        self.B_IMAGE_V.grid(row=1,column=3,padx=50,pady=20)

        self.C1_IMAGE_V = Label(self.sixth_frame,image=self.C1_IMAGE)
        self.C1_IMAGE_V.grid(row=1,column=1,padx=50,pady=20)

        self.C2_IMAGE_V = Label(self.sixth_frame,image=self.C2_IMAGE)
        self.C2_IMAGE_V.grid(row=1,column=2,padx=50,pady=20)

        self.C3_IMAGE_V = Label(self.sixth_frame,image=self.C3_IMAGE)
        self.C3_IMAGE_V.grid(row=1,column=3,padx=50,pady=20)

        self.C4_IMAGE_V = Label(self.sixth_frame,image=self.C4_IMAGE)
        self.C4_IMAGE_V.grid(row=1,column=4,padx=50,pady=20)


        self.FULL_BOX = Entry(self.sixth_frame,textvariable=self.FULL_BOX_String, bg="white")
        self.FULL_BOX.grid(row=2,column=1,padx=50,pady=10)
        self.FULL_BOX.config(fg="black",justify="center")
        self.FULL_BOX.config(bd=10)
        self.FULL_BOX.config(relief="groove")

        self.EMPTY_BOX = Entry(self.sixth_frame,textvariable=self.EMPTY_BOX_String, bg="white")
        self.EMPTY_BOX.grid(row=2,column=2,padx=50,pady=10)
        self.EMPTY_BOX.config(fg="black",justify="center")
        self.EMPTY_BOX.config(bd=10)
        self.EMPTY_BOX.config(relief="groove")

        self.BOX_ENTRY = Entry(self.sixth_frame,textvariable=self.BOX_ENTRY_String, bg="white")
        self.BOX_ENTRY.grid(row=2,column=3,padx=50,pady=10)
        self.BOX_ENTRY.config(fg="black",justify="center")
        self.BOX_ENTRY.config(bd=10)
        self.BOX_ENTRY.config(relief="groove")

        self.BOX_EXIT = Entry(self.sixth_frame,textvariable=self.BOX_EXIT_String, bg="white")
        self.BOX_EXIT.grid(row=2,column=4,padx=50,pady=10)
        self.BOX_EXIT.config(fg="black",justify="center")
        self.BOX_EXIT.config(bd=10)
        self.BOX_EXIT.config(relief="groove")
        #self.root.after(3,self.connect_push)
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