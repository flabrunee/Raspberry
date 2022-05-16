#!/usr/bin/env python3
import time
import os
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
client = ModbusClient('192.168.100.156', port=502)
client.connect()

UNIT = 0x1
0000000000

num = str
num1 = "005218430501069805D2211222"
cont = 0
num2 = 0
#write = client.write_register(4, 1, unit=UNIT)#escribe la palabra 4 a uno
#time.sleep(1)
#write = client.write_register(4, 0, unit=UNIT)#escribe la palabra 4 a cero

while True:
    read = client.read_holding_registers(2, 1, unit=UNIT)# lee la palabra 2
    if read.registers[0]==1:
        print("imprimiendo")
        #os.system("lp et.prn")
        if num2==0:
            num = (input ("introduzca un codigo " ))
        if num==num1:
            cont=cont + 1
            correcto=" correcto " + time.strftime("%H:%M:%S ") + time.strftime("%d/%m/%y  ") + "\n" + "piezas ok " + str(cont) + "\n"
            print (correcto)
            archivo = open ("historico.txt", "a")
            write = client.write_register(0, 1, unit=UNIT)# escribe la palabra 0 a uno para liberar
            time.sleep(0.1)
            archivo.write ( num1 + "\n" + correcto + "\n")
            archivo.close ()
            num=0
            num2=0
            write = client.write_register(0, 0, unit=UNIT)# escribe la palabra 0 a cero para reiniciar

client.close()