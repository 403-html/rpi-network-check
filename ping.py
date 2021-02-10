#!/usr/bin/env python
# written in Py 2.7
import os
import platform
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

def now_date():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

safe_open_w(file_path)

class Date_Chunk:
    def __init__ (self, start = None, end = None):
        self.start_date = start
        self.end_date = end
    
    def update_start_date(self):
        self.start_date = now_date()

    def update_end_date(self):
        self.end_date = now_date()

ans = None
loop_count = 0

while True:
    if ans == "q":
        break

    chunk = Date_Chunk()

    try:
        response = os.system("ping -c 1 {} > /dev/null".format(hostname))

        loop_count += 1
        print("Working loop: {}".format(loop_count))

        if not response == 0:
            print("{}, is down!".format(hostname))
            if chunk.start_date == None:
                chunk.update_start_date()
            elif chunk.end_date == None:
                chunk.update_end_date()
            else:
                with open(file_path, "w") as f:
                    f.write("Net not working, from {} to {}".format(chunk.start_date, chunk.end_date))
                    f.close()
                break
        time.sleep(0.5)
    except KeyboardInterrupt:
        ans = "q"
        pass