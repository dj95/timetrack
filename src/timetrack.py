#!/usr/bin/env python3
#
# timetrack
#
# (c) 2016 Daniel Jankowski


from modules.ManagementThread import *
from modules.utils import *


NAME = 'Daniel Jankowski'


def main():
    # set the log level for debug purposes
    set_log_level(3)
    log('norm', 'Starting time-track')
    # start the management thread
    management_thread = ManagementThread(NAME)
    management_thread.start()


if __name__ == '__main__':
    main()
