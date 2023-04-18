#!/usr/bin/python3
import sqlite3
import serial
import time

#Get the time and date of data point
date = time.strftime("%Y-%m-%d")
time = time.strftime("%H:%M:%S")

#Send byte sequence over serial, read temperature output as a float
ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 5)
ser.write(b'GET DATA')
temp_kelvin = float(ser.readline().decode().strip())
ser.close()

#Convert kelvin to fahrenheit
temp_f = 1.8*temp_kelvin - 459.4

s = sqlite3.connect('data.db')
c = s.cursor()

print(type(temp_f))
print(type(date))
print(type(time))

try:
    c.execute("insert into data values (temp_f, date, time);")
    s.commit()
except:
    print('Error storing data in database');

s.close()
