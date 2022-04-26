# Python program to explain the
# use of join() method in Thread class

import time
import threading


def thread_1(i):  # Por su demora se ubica en segunda posicion
    time.sleep(2)
    print('Value by Thread 1:', i)


def thread_2(i):  # El hilo que mas tarda en ejecutarse
    time.sleep(5)
    print('Value by Thread 2:', i)


def thread_3(i):  # El hilo que mas rapido termina
    print('Value by Thread 3:', i)


# Creating three sample threads
thread1 = threading.Thread(target=thread_1, args=(1,))
thread2 = threading.Thread(target=thread_2, args=(2,))
thread3 = threading.Thread(target=thread_3, args=(3,))

# Running three thread object
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()

print()
# Creating another 3 threads
thread4 = threading.Thread(target=thread_1, args=(1,))
thread5 = threading.Thread(target=thread_2, args=(2,))
thread6 = threading.Thread(target=thread_3, args=(3,))

thread4.start()
thread5.start()
thread6.start()
thread4.join()
thread5.join()
thread6.join()
