#!/usr/bin/env python3
#
# timetrack
#
# (c) 2016 Daniel Jankowski


import gi
import os
import time
import socket
import datetime


gi.require_version('Notify', '0.7')


from gi.repository import Notify
from threading import Thread, Event



try:
    from utils import *
    from evaluate import *
except Exception as e:
    from modules.utils import *
    from modules.evaluate import *


class ManagementThread(Thread):

    def __init__(self, name):
        super().__init__()

        # create stop event for thread
        self.stop_event = Event()

        # initialize unix socket
        try:
            self.__socket = socket.socket(socket.AF_UNIX, socket.SOCK_RAW)
            self.__socket.bind('/dev/shm/timetrackpy.socket')
            self.__socket.settimeout(1.0)
        except Exception as e: # If this doesnt work, remove existing
            log('warn', 'Deleted old socket')
            os.remove('/dev/shm/timetrackpy.socket')
            self.__socket = socket.socket(socket.AF_UNIX, socket.SOCK_RAW)
            self.__socket.bind('/dev/shm/timetrackpy.socket')
            self.__socket.settimeout(1.0)

        # some constants
        self.__data_path = os.path.expanduser('~/Timetrack/data/timetrack.data')
        self.__name = name

        # Initialize connection to libnotify.
        Notify.init("timetrack")

    def __shutdown(self):
        # remove unix socket
        os.remove('/dev/shm/timetrackpy.socket')
        return

    def __start_time(self):
        # get current unix timestamp
        timestamp = time.time()
        # format the time stamp
        actual_time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        # write it with prefix to file
        write_to_file(self.__data_path, 'START_{0}\n'.format(timestamp))

        # Print notification with libnotify.
        notification = Notify.Notification.new("TimeTrack", "Started working: {time}".format(time=actual_time), "dialog-information")
        notification.show()
        return

    def __stop_time(self):
        # get current unix timestamp
        timestamp = time.time()
        # format the time stamp
        actual_time = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
        # write it with prefix to file
        write_to_file(self.__data_path, 'STOP_{0}\n'.format(timestamp))

        # Print notification with libnotify.
        notification = Notify.Notification.new("TimeTrack", "Stopped working: {time}".format(time=actual_time), "dialog-information")
        notification.show()
        return

    def run(self):
        # thread loop
        while not self.stop_event.is_set():
            # try to read data from socket
            try:
                data = self.__socket.recv(1024)
            except: # if no data is available, continue to next try
                continue
            # decode data
            ws = data.decode('utf-8')
            
            # check for command and run it
            if ws == 'CMDstart': # start command
                self.__start_time()
            elif ws == 'CMDstop': # stop command
                self.__stop_time()
            elif ws == 'CMDevaluate': # evaluate command
                log('info', 'Evaluating data')
                # initialize the evaluator
                evaluator = Evaluator(self.__data_path)
                # read the data and process it
                evaluator.read_data()
                # generate html code and write it to file
                evaluator.generate_html(self.__name)
            # short timeout to save performance
            self.stop_event.wait(1.0)
        # shutdown
        self.__shutdown()
