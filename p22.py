#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading
import usb.core
import usb.util
from time import sleep

global dev

##### Capturar lectora Elitronic
devElit = usb.core.find(idVendor=0x0483, idProduct=0x5710)
#print (dev[0])
if dev is None:
       print('Disp no encontrado')
else:
       print('Lectora Elitronic encontrada')
#       if dev.is_kernel_driver_active(0):
#               try:
#                       dev.detach_kernel_driver(0)
#               except:
#                       print("error dev.detach_kernel_driver(0)")
#                       pass
#       print (usb.util.get_string(dev, dev.idProduct))

##### Desconectar dispositivo del driver para poder hacer operaciones de E/S
c = 0
for config in dev:
       print('config', c)
        for i in range(config.bNumInterfaces):
               if dev.is_kernel_driver_active(i):
                       dev.detach_kernel_driver(i)
                print(i)
        c += 1
### Esto nunca anda --> dev.set_configuration()

#while True:
##### Intento de lectura 952
"""
data1 = ''
try:
        print('1')
#       while data1 == '':
        data1 = dev.read(0x81, 7, timeout = 0)
        print(data1)
        print('2')
        if data1 != '':
                print(data1)
except:
        print('Error')
#    except usb.core.USBError as e:
#        if e.args == ('Operation timed out'):
        pass
"""
###Intento de lectura 1254
endpoint = dev[0][(0, 0)][0]
data2 = []
lu = False
print("Waiting to read...")
lecture = ''

while 1:
    try:
        data2 += dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        print(data2)
    except:
        #        print('No anduvo')
        continue

'''
        if not lu:
            print "Waiting to read..."
        lu = True

    except usb.core.USBError as e:
        if e.args == (110,'Operation timed out') and lu:
            if len(data2) < DATA_SIZE:
                print "Lecture incorrecte, recommencez. (%d bytes)" % len(data2)
                print "Data: %s" % ''.join(map(hex, data2))
                data2 = []
                lu = False
                continue
            else:
                for n in range(0,len(data2),16):
                    print ' '.join(map(hex,data2[n:n+16]))
                    lecture+=NO_SCAN_CODE[data2[n+2]]
                break   # Code lu
return lecture
'''

#dev.set_configuration()
print("Terminó")
