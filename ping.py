#!/usr/bin/env python3

import errno
import os
import time
import typing
from datetime import datetime

from custom_logger import logger

# To store config consider python_dotenv
HOSTNAME = '8.8.8.8'
FILE_NAME = 'ping.txt'
FILE_DIR = './tmp/'
FILE_PATH = '{}{}'.format(FILE_DIR, FILE_NAME)


def file_path(file_dir: str, file_name: str) -> str:
    """Return path to provided file."""
    path_to_file = os.path.join(os.path.dirname(file_dir), file_name)
    return path_to_file


def is_path_present(path: str) -> bool:
    """Check if path exists in file system."""
    return os.path.exists(path)


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise exc


def safe_open_w(path):
    mkdir_p(os.path.dirname(path))
    return open(path, 'w')


def now_date() -> str:
    now = datetime.now()
    dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
    return dt_string


safe_open_w(file_path(FILE_DIR, FILE_NAME))


class DateChunk:
    """TODO: Add description"""
    start_date: typing.Optional[str]
    end_date: typing.Optional[str]
    
    def update_start_date(self) -> None:
        """TODO: Add description"""
        self.start_date = now_date()

    def update_end_date(self) -> None:
        """TODO: Add description"""
        self.end_date = now_date()


ans = None
loop_count = 0

while True:
    if ans == 'q':
        break

    chunk = DateChunk()

    try:
        response = os.system(f'ping -c 1 {HOSTNAME} > /dev/null')

        loop_count += 1
        logger.info('Working loop: %s', loop_count)

        if not response == 0:
            logger.info('%s, is down!', HOSTNAME)
            chunk.update_start_date()

            while True:
                response = os.system(f'ping -c 1 {HOSTNAME} > /dev/null')

                if response == 0:
                    chunk.update_end_date()

                    message = 'Net not working, from {} to {}\n'.format(chunk.start_date, chunk.end_date)
                    logger.error(message)
                    
                    with open(file_path(FILE_DIR, FILE_NAME), 'a+') as f:
                        f.write(message)
                    break
        time.sleep(0.5)
    except KeyboardInterrupt:
        ans = 'q'
        pass
