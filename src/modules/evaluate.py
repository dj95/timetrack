#!/usr/bin/env python3
#
# timetrack
#
# (c) 2016 Daniel Jankowski


import os
import time
import datetime


class Evaluator(object):

    def __init__(self, data_path):
        # constructor of the object
        super().__init__()

        # some class variables
        self.__data_path = data_path
        self.__data = {}

    def read_data(self):
        """
        Read the data from the data file and process the data to a dictionary.
        """
        # check if the file exists
        if not os.path.isfile(self.__data_path):
            print('==> Error: No data path')
            return

        # read data from file
        with open(self.__data_path, 'r') as fp:
            data = fp.readlines()

        # iterate through file lines
        for i in range(0, len(data), 2):
            # check if a stop timestamp follows a start timestamp
            if data[i].startswith('START') and not data[i + 1].startswith('STOP'):
                # get start timestamp from the data
                start_time = float(data[i][:-1].split('_')[1])

                # convert timestamps to readable date
                start_time = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')

                # append broken data to dict
                self.__data[start_time] = 'Inconsistent data'
                i = i - 1
                continue

            # get start and end timestamp from the data
            start_time = float(data[i][:-1].split('_')[1])
            end_time = float(data[i + 1][:-1].split('_')[1])

            # convert timestamps to readable date
            start_time = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.fromtimestamp(end_time).strftime('%Y-%m-%d %H:%M:%S')
           
            # append the data
            self.__data[start_time] = end_time
        return self.__data

    def generate_html(self, name):
        # read the html template
        with open('./modules/html/index.html', 'r') as fp:
            html = fp.read()
        
        table = ''
        # iterate through the times dictionary
        for date in sorted(self.__data.keys()):
            # get date
            entry_date = date.split(' ')[0]
            # get start time
            start_time = date.split(' ')[1]
            # check for inconsistent data
            if self.__data[date].startswith('Inco'):
                end_time = self.__data[date]
                length = '-'
            else:
                end_time = self.__data[date].split(' ')[1]

                # calculate work length
                length = (datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))

            # create table
            table += """                <tr>
                    <td>{date}</td>
                    <td style="text-align: center;">{start}</td>
                    <td style="text-align: center;">{end}</td>
                    <td style="text-align: right;">{length}</td>
                </tr>\n""".format(date=entry_date, start=start_time, end=end_time, length=length)
        html = html.format(name=name, table=table)
        
        # write html to file
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
        with open(os.path.expanduser('~/Timetrack/Timetrack_{time}.html'.format(time=timestamp)), 'w') as fp:
            fp.write(html)
