import serial
import threading
import time
import re

#TODO: iter and speed_value input from import
from device_classes import Tensiometer

ser = serial.Serial('COM4', 115200, timeout=1)

time.sleep(2)

def read_data():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(data + "\n")

def write_manual():
    while True:
        manual = input() # manual == 0 or 1
        ser.write((manual + '\n').encode('utf-8'))

def write_speed():
    while True:
        speed_value = input()
        ser.write((speed_value + '\n').encode('utf-8'))

def write_iter():
    while True:
        speed_value = input()
        ser.write((speed_value + '\n').encode('utf-8'))


read_thread = threading.Thread(target=read_data, daemon=True)
read_thread.start()

write_thread_manual = threading.Thread(target=write_manual, daemon=True)
write_thread_manual.start()

# write_thread_speed = threading.Thread(target=write_speed, daemon=True)
# write_thread_speed.start()

# iter = input()
# write_speed(iter)

