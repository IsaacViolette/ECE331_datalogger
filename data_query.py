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

#Open database connection
s = sqlite3.connect('data.db')
c = s.cursor()

#Insert data into sql database, if it doesn't work, print error message
try:
    c.execute("insert into data values (?,?,?);",(temp_f,date,time))
    s.commit()
except:
    print('Error storing data in database');

#Close database connection
s.close()
