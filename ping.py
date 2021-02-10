#!/usr/bin/env python
# written in Py 2.7
import os
import errno
import time
from datetime import datetime
hostname = "8.8.8.8"
filename = "ping.txt"
file_dir = "./tmp/"
file_path = "{}{}".format(file_dir, filename)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: raise

def safe_open_w(path):
    mkdir_p(os.path.dirname(path))
    return open(path, 'w')

with safe_open_w(file_path) as f: pass

def now_date():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

class Date_Chunk:
    def __init__ (self, start = None, end = None):
        self.start_date = start
        self.end_date = end
    
    def update_start_date():
        self.start_date = now_date()

    def update_end_date():
        self.start_date = now_date()

ans = None
while True:
    if ans == "q":
        break

    chunk = Date_Chunk()

    try:
        response = os.system("ping -c 1 {} > /dev/null".format(hostname))
        if response == 0:
            print hostname, 'is up!'
        else:
            print hostname, 'is down!'
        time.sleep(0.5)
    except KeyboardInterrupt:
        ans = "q"
        pass