# -*- coding: utf-8 -*-
"""
La forma de trabajo de las lectoras es con hilos (no multitarea real)* porque el host controlador de USB trabaja
con un dispositivo a la vez, no por nada se llama (Univ SERIAL Bus). Ref: https://nxmnpg.lemoda.net/4/usb
*Cada hilo se duerme un tiempo (~0.5seg) despues de terminar su proceso, para que el otro hilo pueda acceder a su lectora.
"""

#TODO #libusb_claim_interface() libusb_release_interface() https://libusb.sourceforge.io/api-1.0/group__libusb__dev.html#ga785ddea63a2b9bcb879a614ca4867bed
#TODO PyUSB: detect device unplug https://stackoverflow.com/questions/40785371/pyusb-detect-device-unplug
#TODO Usar Lock() para que el hilo tenga acceso unico https://docs.python.org/es/3/library/multiprocessing.html#synchronization-between-processes
#     https://docs.python.org/2/library/thread.html#thread.lock.locked

import _thread
import threading
import usb.core
import usb.util
from collections import namedtuple
from time import sleep

""" class classLectora:
    idVnd = ''
    idProd = '' """

#Estructura para guardar los id de las lectoras
lectora = namedtuple('lectora', ['nombre', 'idVnd', 'idProd'])
#Bandera para terminar los hilos
finalizarHilo = False


charmap0 = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm',
            17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y',
            29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ',
            45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';', 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}

charmap2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M',
            17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y',
            29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ',
            45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}


def inicializarLectora(lectoraparam):
    #Buscar lectora en el arbol USB
    lectHndlr = usb.core.find(
        idVendor=lectoraparam.idVnd, idProduct=lectoraparam.idProd)
    if lectHndlr is None:
        print("Lectora ", lectHndlr.nombre, " no conectada")
    #Desconectar dispositivo del driver para poder hacer operaciones de E/S
    if lectHndlr.is_kernel_driver_active(0):
        try:
            lectHndlr.detach_kernel_driver(0)
        except usb.core.USBError as e:
            print("No se pudo desconectar del driver: %s" % str(e))
    return lectHndlr


def leer(lectoraparam):
    #Endpoint
    EP = lectoraparam.device[0][(0, 0)][0]
    termina = False
    while not finalizarHilo:
        while not termina:
            data = []
            dataList = []
            shift = False  # Bandera para cuando vienen mayusculas
            try:
                buffer = lectoraparam.read(
                    EP.bEndpointAddress, EP.wMaxPacketSize, timeout=99999999999999999)
            except usb.core.USBError as e:
                buffer = ""
                if e.args == ('Operation timed out',):
                    # TODO La idea es hacer algo mas si da error de timeout
                    print(e.args)
                pass
            ss = ""
            for c in buffer:
                digito = ord(c)
                if digito > 0:
                    if int(digito) == 40:
                        termina = True
                        break
                    if int(digito) == 2:  # Las siguientes son mayusculas
                        shift = True
                    elif shift:
                        ss += charmap2[int(ord(c))]
                    else:
                        ss += charmap0[int(ord(c))]
                #Ver Lectoras.py
        print(ss)
        sleep(1)


#def convertir():


if __name__ == "__main__":
    try:
        #Crear instancias de lectoras pasando los identificadores
        lectHW = lectora('Honeywell', '0c2e', '1001')
        lectEli = lectora('Elitronic', '0483', '5710')
        #Buscar la lectora, inicializarla y obtener Handler del dispositivo
        lectHWHdlr = inicializarLectora(lectHW)
        lectEliHdlr = inicializarLectora(lectEli)
        #Crear hilos de lectura
        lectHWThrd = threading.Thread(
            name='lectHW', target=leer, args=(lectHWHdlr,))
        lectEliThrd = threading.Thread(  # TODO Comprobar si no hace falta crear otra funcion para la segunda lectora
            name='lectEli', target=leer, args=(lectEliHdlr,))
        #Comenzar hilos
        lectHWThrd.start()
        lectEliThrd.start()
        # Sin el join la ejecucion sigue su curso (imprime 'Terminado') pero sin terminar el programa (hasta que terminan los hilos).
        lectHWThrd.join()
        lectEliThrd.join()
        # Con el join se bloquea la ejecucion del programa hasta que termina ese hilo.
        print('Terminado')
    except Exception:
        finalizarHilo = True
        # raise KeyboardInterrupt  Generar Ctrl+Pause
        print("Error")
    except KeyboardInterrupt:
        finalizarHilo = True
        #  exit(?)  # TODO ver como reenviar el codigo de error y la forma limpia de terminar el hilo del main.
        print('Error')
        exit(0)
