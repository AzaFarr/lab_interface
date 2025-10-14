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

def write_loc():
    while True:
        loc = input()
        ser.write((loc + '\n').encode('utf-8'))

def write_speed():
    while True:
        speed_value = input()
        ser.write((speed_value + '\n').encode('utf-8'))

def write_iter():
    while True:
        speed_value = input()
        ser.write((speed_value + '\n').encode('utf-8'))

# def write_autom():
#     while True:
#         autom = input()
#         ser.write((autom + '\n').encode('utf-8'))
#
# def write_manual():
#     while True:
#         manual = input()
#         ser.write((manual + '\n').encode('utf-8'))
#
# def write_glob():
#     while True:
#         glob = input()
#         ser.write((glob + '\n').encode('utf-8'))

read_thread = threading.Thread(target=read_data, daemon=True)
write_loc_thread = threading.Thread(target=write_loc, daemon=True)
write_thread_speed = threading.Thread(target=write_speed, daemon=True)
write_thread_iter = threading.Thread(target=write_iter, daemon=True)
# write_autom_thread = threading.Thread(target=write_autom, daemon=True)
# write_manual_thread = threading.Thread(target=write_manual, daemon=True)
# write_glob_thread = threading.Thread(target=write_glob, daemon=True)


read_thread.start()
write_loc_thread.start()
write_thread_speed.start()
write_thread_iter.start()
# write_autom_thread.start()
# write_manual_thread.start()
# write_glob_thread.start()








