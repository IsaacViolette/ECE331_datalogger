#!/usr/bin/python3

import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

time_now = datetime.now()
dayAgo = datetime.now() - timedelta(hours=24)

s = sqlite3.connect('data.db')
c = s.cursor()

data = []
try:
    c.execute("select * from data where datetime >= '{dayAgo}'")
    for row in c.fetchall():
        print(row[0])
        print(row[1])
except:
    print("Could not retrieve data from database")

