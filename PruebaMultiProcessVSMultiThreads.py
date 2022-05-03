#Prueba de Multithreading


import time
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

   print(f'Tiempo transcurrido {time.time() - start }')

#----------------------------------------------------------------
#Prueba de Multiprocesos
""" import time
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

   print(f'Tiempo transcurrido {time.time() - start }') """

#----------------------------------------------------------------
#Prueba de Multihilos con Pool de hilos https://python-para-impacientes.blogspot.com/2016/12/threading-programacion-con-hilos-i.html


""" import threading
    def contar():
    contador = 0
    while contador < 100:
        contador += 1
        print('Hilo:',
              threading.current_thread().name(),
              'con identificador:',
              threading.current_thread().ident,
              'Contador:', contador)


NUM_HILOS = 3

for num_hilo in range(NUM_HILOS):
    hilo = threading.Thread(name='hilo%s' % num_hilo,
                            target=contar)
    hilo.start() """
