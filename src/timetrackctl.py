#!/usr/bin/env python3
#
# timetrack
#
# (c) 2016 Daniel Jankowski


import socket
import argparse


ALLOWED_COMMANDS = ['start', 'stop', 'evaluate']


def send_command(command):
    # open socket
    s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    s.connect('/dev/shm/timetrackpy.socket')
    # send command over socket
    s.send('CMD{0}'.format(command).encode('utf-8'))
    # close socket connection
    s.close()


def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    args = parser.parse_args()

    # check if argument is in the allowed commands
    if args.command in ALLOWED_COMMANDS:
        # send the command over the unix socket
        send_command(args.command)
    else:
        print('==> Error: Command not allowed')


if __name__ == '__main__':
    main()
