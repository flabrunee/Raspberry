# -*- coding: utf-8 -*-
import _thread
from time import sleep
from threading import Thread
import os


class myClass():

    def help(self):
       # cmd = 'notepad.exe'
       # os.system(cmd)  # ('./ssh.py')
        a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        for i in a:
            print(i)
            sleep(0.5)

    def nope(self):
        a = [1, 2, 3, 4, 5, 6, 67, 78]
        for i in a:
            print(i)
            sleep(0.4)


if __name__ == "__main__":
    Yep = myClass()
    thread = Thread(target=Yep.help)
    thread2 = Thread(target=Yep.nope)
    thread.start()
    thread2.start()
    # Sin el join la ejecucion sigue su curso (imprime 'Finished') pero sin terminar el programa (hasta que terminan los hilos).
    thread2.join()
    #Con el join se bloquea la ejecucion del programa hasta que termina ese hilo.
    print('Finished')
