import serial
import time
arduino = serial.Serial("/dev/ttyS4")
time.sleep(2)
arduino.write(b"1")
arduino.close()