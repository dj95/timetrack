#!/usr/bin/env python3
#
# timetrack
#
# (c) 2016 Daniel Jankowski


import os


log_level = 0


def set_log_level(level):
    """
    Sets the global constant for the log level.
    """
    global log_level
    log_level = level


def log(tag, text):
    """
    Logs text to the console or appends them to the logfile,
    depending on the log level.
    """
    if tag == 'norm'  and log_level >= 2: # normal tag
        print('\033[92m==>\033[0m {0}'.format(text))
    elif tag == 'info'  and log_level >= 3: # info tag
        print('\033[94m ->\033[0m {0}'.format(text))
    elif tag == 'warn'  and log_level >= 1: # warning tag
        print('\033[93m==> Warning:\033[0m {0}'.format(text))
    elif tag == 'err'  and log_level >= 0: # error tag
        print('\033[91m==> Error:\033[0m {0}'.format(text))


def write_to_file(path, text):
    with open(path, 'a') as fp:
        fp.write(text)
