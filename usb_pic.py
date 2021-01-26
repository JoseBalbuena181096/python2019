#!/usr/bin/env python3
  
import usb.core
import usb.util
import sys
import time
  
#next line sets Vendor/Product id, these values have to be set also in PIC-side
#You can check the set values in linux using command "lsusb". This shows ID VendorId:ProductId
dev =  usb.core.find(idVendor=0x2405 ,idProduct=0x000b ) 
  
#When you connect the device to linux. Linux automatically sets some drivers to it. In order to this script to work
#we must first detach the driver
if dev.is_kernel_driver_active(0) is True:
    dev.detach_kernel_driver(0)
  
if dev is None:
    raise ValueError('Device not found')
  
dev.set_configuration()
print("Device Found!")
print(dev)
while True:
    print("Enter E to turn on or Enter A to turn off or T to end")
    choice = input()
    if choice == "E":
        dev.write(2,'E',100)
        dev.write(2,'E',100)
    elif choice == "A": 
        dev.write(2,'A',100)
        dev.write(2,'A',100)
    elif choice == 'T':
        break