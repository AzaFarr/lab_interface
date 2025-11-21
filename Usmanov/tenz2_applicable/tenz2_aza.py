import serial
import threading
import time
import re

#TODO: iter and speed_value input from import
from device_classes import Tensiometer

ser = serial.Serial('COM3', 115200, timeout=1)

time.sleep(2)

def read_data():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(data + "\n")

def write():
    while True:
        value = input()
        ser.write((value + '\n').encode('utf-8'))


read_thread = threading.Thread(target=read_data, daemon=True)

read_thread.start()
write()



