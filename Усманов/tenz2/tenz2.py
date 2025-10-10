import serial
import threading
import time

#TODO: iter and speed_value input from import
from device_classes import Tensiometer

ser = serial.Serial('COM4', 115200, timeout=1)

time.sleep(2)

def read():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(f"From Arduino: {data}")

def write(data):
    while True:
        iter, speed_value = data
        ser.write((iter + '\n').encode('utf-8'))
        ser.write((speed_value + '\n').encode('utf-8'))

read_thread = threading.Thread(target=read, daemon=True)
read_thread.start()

iter = input()
speed_value = input()
write((iter, speed_value))
