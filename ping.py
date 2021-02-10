#!/usr/bin/env python
# written in Py 2.7
import os
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

