#!/usr/bin/env python3
#
# timetrack
#
# (c) 2016 Daniel Jankowski


from threading import Thread, Event


class ManagementThread(Thread):

    def __init__(self):
        super().__init()

        self.stop_event = Event()

    def __shutdown(self):
        return

    def run(self):
        while not self.stop_event.is_set():
            print('s')
            self.stop_even.sleep(1.0)
        self.__shutdown()
