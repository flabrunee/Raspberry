#Prueba de Multithreading
""" import time
import threading


def countdown(number):
   while number > 0:
      number -= 1


if __name__ == '__main__':
   start = time.time()

   count = 100000000

   t1 = threading.Thread(target=countdown, args=(count,))
   t2 = threading.Thread(target=countdown, args=(count,))

   t1.start()
   t2.start()

   t1.join()
   t2.join()

   print(f'Tiempo transcurrido {time.time() - start }') """

#----------------------------------------------------------------
#Prueba de Multiprocesos
import time
import threading
import multiprocessing


def countdown(number):
   while number > 0:
      number -= 1


if __name__ == '__main__':
   start = time.time()

   count = 100000000

   t1 = multiprocessing.Process(target=countdown, args=(count,))
   t2 = multiprocessing.Process(target=countdown, args=(count,))

   t1.start()
   t2.start()

   t1.join()
   t2.join()

   print(f'Tiempo transcurrido {time.time() - start }')
