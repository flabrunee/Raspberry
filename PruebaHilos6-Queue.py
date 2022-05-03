#Ejemplo de threads compartiendo una variable con Queue
#https://stackoverflow.com/questions/61620151/how-to-get-data-from-a-thread-in-real-time?noredirect=1&lq=1

#import threading
#import queue
from multiprocessing import Pipe


def one(connA):  # def one()
  while True:                                           #while True:
    a = data1                                           #   a = data1
    connA.send([a])
                                                        #something gonna here with var b from thread two

def two(connB):                                         #def two()
  while True:                                           #while True:
    b = connB.recv() #receives [a] from thread one      #   b = a from thread one
    connB.send([b]) #send [b] to main thread            #   something gonna here
    
def main():                                             #def main():
  A,B=Pipe()
  th1 = Thread(target=one,args=(A))                     #   th1 = Thread(target=one)
  th2 = Thread(target=two,args=(B))                     #   th2 = Thread(target=two)
  th1.start()                                           #   th1.start()
  th2.start()                                           #   th2.start()
                                                        #   something gonna here with var a and var b
  b=A.recv() # receive var b from 