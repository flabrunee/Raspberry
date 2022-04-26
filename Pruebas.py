# -*- coding: utf-8 -*-
import _thread
from time import sleep
from threading import Thread


class myClass():

    def help(self):
        os.system('./ssh.py')

    def nope(self):
        a = [1, 2, 3, 4, 5, 6, 67, 78]
        for i in a:
            print(i)
            sleep(1)


if __name__ == "__main__":
    Yep = myClass()
    thread = Thread(target=Yep.help)
    thread2 = Thread(target=Yep.nope)
    thread.start()
    thread2.start()
    thread.join()
    print('Finished')
