#!/usr/bin/python3

import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
import pytz

time_now = datetime.now()
dayAgo = datetime.now() - timedelta(hours=24)

s = sqlite3.connect('data.db')
c = s.cursor()

try:
    c.execute("select * from data where datetime >= ?", (dayAgo,))
    s.commit()
except:
    print("Could not retrieve data from database")

data = []
for row in c.fetchall():
    temp_f = (row[1] - 273.15) * 9/5 + 32
    UTC_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
    UTC_tz = pytz.timezone('UTC')
    UTC_time = UTC_tz.localize(UTC_time)
    EST_tz = pytz.timezone('US/Eastern')
    EST_time = UTC_time.astimezone(EST_tz)
    EST_time_string = EST_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    data.append((EST_time_string, temp_f))

print(data)

s.close()
