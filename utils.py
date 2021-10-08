from threading import Thread
import time

class Interval(Thread):
    """
    Run a function on a given interval
    """

    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.running = False

    def start(self):
        time1 = time.time_ns() // 1_000_000 

        while not self.running:
            time2 = time.time_ns() // 1_000_000 
            if time2 - time1 >= self.interval:
                self.action()
                time1 = time2


    def stop(self):
        self.running = True
