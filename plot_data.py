#!/usr/bin/python3

import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pytz
import numpy as np
#from scipy.interpolate import make_interp_spline

time_now = datetime.now()
dayAgo = datetime.now() - timedelta(hours=24)

s = sqlite3.connect('/home/iviolette/datalogger/data.db')
c = s.cursor()

try:
    c.execute("select * from data where datetime >= ?", (dayAgo,))
    s.commit()
except:
    print("Could not retrieve data from database")

datetime_data = []
temp_data = []
time_data = []
for row in c.fetchall():
    temp_f = (row[1] - 273.15) * 9/5 + 32
    UTC_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
    UTC_tz = pytz.timezone('UTC')
    UTC_time = UTC_tz.localize(UTC_time)
    EST_tz = pytz.timezone('US/Eastern')
    EST_time = UTC_time.astimezone(EST_tz)
    EST_datetime_string = EST_time.strftime('%Y-%m-%d %H:%M')
    EST_time_string = EST_time.strftime('%H:%M')
    datetime_data.append(EST_datetime_string)
    temp_data.append(temp_f)
    time_data.append(EST_time_string)

s.close()


datetime_np = np.array(datetime_data)
temp_np = np.array(temp_data)
time_np = np.array(time_data)

plt.figure(figsize=(14,6))
plt.plot(time_np,temp_np)

xticks = np.linspace(0, 1440, 13)
plt.xticks(xticks,rotation=15,fontsize=10)

plt.xlabel('Time')
plt.ylabel('Temperature (F)')
plt.title(f'Temperature from {datetime_np[0]} to {datetime_np[-1]}')
plt.grid()
plt.savefig("/var/www/html/temp_plot.png", dpi=250)


