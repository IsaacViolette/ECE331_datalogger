#!/usr/bin/python3

import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

time_now = datetime.now()
dayAgo = datetime.now() - timedelta(hours=24)

s = sqlite3.connect('data.db')
c = s.cursor()

try:
    c.execute("select * from data where datetime >= '{dayAgo}';")
    s.commit()
except:
    print("Could not retrieve data from database")

# data = []
# for row in c.fetchall():
#    print(row[0])
#    print(row[1])

print(c.fetchall())

s.close()
