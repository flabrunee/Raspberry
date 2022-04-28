# Ejemplo con una variable compartida entre threads
# https://stackoverflow.com/questions/68535687/python-threads-using-the-same-variables?noredirect=1&lq=1

# -*- coding: utf-8 -*-
import threading
import time

can_run = True
downspeed = 0


def updating():
    global downspeed
    while can_run:
        downspeed = downspeed+1
        time.sleep(0.1)   # Allow taskswitches


def main():
    while can_run:
        print(downspeed)
        time.sleep(1)   # Allow taskswitches


u = threading.Thread(name='background', target=updating)
m = threading.Thread(name='foreground', target=main)

u.start()
m.start()

time.sleep(10)  # Allow time for the threads to do what they want
can_run = False
print('Done')
u.join()
m.join()
