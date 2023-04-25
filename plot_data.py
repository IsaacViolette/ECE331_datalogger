#!/usr/bin/python3

import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pytz
import numpy as np
from scipy.interpolate import make_interp_spline

time_now = datetime.now()
dayAgo = datetime.now() - timedelta(hours=24)

s = sqlite3.connect('data.db')
c = s.cursor()

try:
    c.execute("select * from data where datetime >= ?", (dayAgo,))
    s.commit()
except:
    print("Could not retrieve data from database")

time_data = []
temp_data = []
for row in c.fetchall():
    temp_f = (row[1] - 273.15) * 9/5 + 32
    UTC_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
    UTC_tz = pytz.timezone('UTC')
    UTC_time = UTC_tz.localize(UTC_time)
    EST_tz = pytz.timezone('US/Eastern')
    EST_time = UTC_time.astimezone(EST_tz)
    EST_time_string = EST_time.strftime('%Y-%m-%d %H:%M')
    time_data.append(EST_time_string)
    temp_data.append(temp_f)

s.close()

#plot_time = [date.timestamp() for date in datetime.strptime(time_data, "%Y-%m-%d")]

time_np = np.array(time_data)
temp_np = np.array(temp_data)

plt.plot(time_np,temp_np)

#X_Y_Spline = make_interp_spline(plot_time,temp_np)
#X_ = np.linspace(min(plot_time), max(plot_time), 1440)
#Y_ = X_Y_Spline(X_)
#plt.plot(X_,Y_)

xticks = np.linspace(0, 1440, 5)
plt.xticks(xticks,rotation=15,fontsize=10)

first = time_np[0]
last = time_np[-1]

plt.xlabel('Date and Time')
plt.ylabel('Temperature (F)')
plt.title(f'Temperature from {first} to {last}')
plt.show()

