#!/usr/bin/python3

import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
import pytz
import numpy as np

def data_plot():

    #Calculate utc time 24 hours ago
    time_now = datetime.now(timezone.utc)
    dayAgo = time_now - timedelta(hours=24)

    #Connect to SQLite3 database
    s = sqlite3.connect('/home/iviolette/datalogger/data.db')
    c = s.cursor()

    #Get all data from now to 1 day ago, print error if it does not work
    try:
        c.execute("select * from data where datetime >= ?", (dayAgo,))
        s.commit()
    except:
        print("Could not retrieve data from database")

    #Arrays for new data
    datetime_data = []
    temp_data = []

    for row in c.fetchall():
        #Convert the temperature data from kelvin to farenheit
        temp_f = (row[1] - 273.15) * 9/5 + 32
        
        #Take the utc datetime data and make it a datetime type
        #Make the naive timezone aware, loalize the UTC time
        UTC_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f')
        UTC_tz = pytz.timezone('UTC')
        UTC_time = UTC_tz.localize(UTC_time)

        #Convert the UTC data to EST, takes care of DST 
        EST_tz = pytz.timezone('US/Eastern')
        EST_time = UTC_time.astimezone(EST_tz)
        
        #Save the new data to new arrays
        datetime_data.append(EST_time)
        temp_data.append(temp_f)

    s.close()

    #Create numpy arrays for data (Not sure if this is needed)
    #datetime_np = np.array(datetime_data)
    temp_np = np.array(temp_data)

    #Plot the figure 14 inches wide and 6 inches tall
    #with auto configured plot
    plt.figure(figsize=(14,6))
    plt.plot(datetime_data,temp_np)
    plt.xlim(dayAgo, time_now)
    plt.gcf().autofmt_xdate()


    #Make the plot more readible with required labels
    plt.xlabel('Time and Date (Month-Day Hour)')
    plt.ylabel('Temperature (F)')
    plt.title(f'Temperature from {datetime_data[0]} to {datetime_data[-1]}')
    plt.grid()

    #Save the plot to the webserver directory where index.php is
    plt.savefig("/var/www/html/temp_plot.png", dpi=250)
