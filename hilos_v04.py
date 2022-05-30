# -*- coding: utf-8 -*-
#ss import _thread
from time import sleep
from threading import Thread
import os
from tkinter import *
from tkinter import ttk
import time
#from pymodbus.client.sync import ModbusTcpClient as ModbusClient

ope = ""
cont = 0
ventana = Tk()
    #Etiqueta Cantidad
lblCant = Label(ventana, text="")
lblCant.place(x=400, y=200)

class myClass():

    def grafica(self):
        global ventana
        
        ventana.title("CARGA DATOS ETIQUETAS")
        ventana.geometry('900x400')
        combo = ttk.Combobox(state="readonly",values=["02000510 FORD", "02000511 FORD", "02000512 FORD", "02000513 FORD", "02000514 FORD", "02000494 FORD", "02000495 FORD", "02000497 FORD", "02000498 FORD", "02000499 FORD", "02000500 FORD", "02000531 FIAT", "02000489 FIAT", "02000490 FIAT", "02000491 FIAT", "02000536 FIAT"])
        combo.place(x=100, y=50)
        global pt
        pt = str()
        global lote
        lote = str()
        global fecha
        fecha = str()
        global juliana
        juliana = StringVar()
        global concern
        concern = StringVar()
        global alert
        alert = StringVar()
        text_lote = StringVar()
        text_fecha = StringVar()
        text_operario = StringVar()
        text_fecha_juliana = StringVar()
        text_concern = StringVar()
        text_alert = StringVar()
        cpo1 = Entry(ventana, font=('arial', 15, 'bold'), width=10, textvariable=text_lote, bd=5, insertwidth=4, bg="powder blue", justify="right").place(x=100, y=100)
        cpo2 = Entry(ventana, font=('arial', 15, 'bold'), width=10, textvariable=text_fecha, bd=5, insertwidth=4, bg="powder blue", justify="right").place(x=100, y=150)
        cpo3 = Entry(ventana, font=('arial', 15, 'bold'), width=10, textvariable=text_operario, bd=5, insertwidth=4, bg="powder blue", justify="right").place(x=100, y=200)
        cpo4 = Entry(ventana, font=('arial', 15, 'bold'), width=10, textvariable=text_fecha_juliana, bd=5, insertwidth=4, bg="powder blue", justify="right").place(x=450, y=50)
        cpo5 = Entry(ventana, font=('arial', 15, 'bold'), width=10, textvariable=text_concern, bd=5, insertwidth=4, bg="powder blue", justify="right").place(x=700, y=50)
        cpo6 = Entry(ventana, font=('arial', 15, 'bold'), width=10, textvariable=text_alert, bd=5, insertwidth=4, bg="powder blue", justify="right").place(x=700, y=100)
        def guardartexto():
            global ope
            global cont
            global lblCant
            
            pt = combo.get()
            if pt=="02000510 FORD":
                pt1="MB3C-5310-FCD"
            if pt=="02000511 FORD":
                pt1="MB3C-5310-FDD"
            if pt=="02000512 FORD":
                pt1="MB3C-5310-FED"
            if pt=="02000513 FORD":
                pt1="MB3C-5310-FFD"
            if pt=="02000514 FORD":
                pt1="MB3C-5310-FGD"
            if pt=="02000494 FORD":
                pt1="JB3C-5310-FAA"
            if pt=="02000495 FORD":
                pt1="JB3C-5310-FBA"
            if pt=="02000497 FORD":
                pt1="JB3C-5310-FDB"
            if pt=="02000498 FORD":
               pt1="JB3C-5310-FEB"
            if pt=="02000499 FORD":
                pt1="JB3C-5310-FFB"
            if pt=="02000500 FORD":
                pt1="JB3C-5310-FGB"
            if pt=="02000531 FIAT":
                pt1="00521843050"
            if pt=="02000489 FIAT":
                pt1="00521007630"
            if pt=="02000490 FIAT":
                pt1="00521007640"
            if pt=="02000491 FIAT":
                pt1="00521007650"
            if pt=="02000536 FIAT":
                pt1="00521965210"
            lbl10.configure(text=pt1)
            lote = text_lote.get()
            lbl11.configure(text=lote)
            fecha = text_fecha.get()
            lbl12.configure(text=fecha)
            ope = text_operario.get()
            lbl13.configure(text=ope)
            juliana = text_fecha_juliana.get()
            lbl14.configure(text=juliana)
            concern = text_concern.get()
            lbl15.configure(text=concern)
            alert = text_alert.get()
            lbl16.configure(text=cont)
               #Inicializar contador
            cont = 0
            lblCant.configure(text=cont)
            
        btn = Button(ventana, text="GUARDAR", command=guardartexto)
        btn.place(x=200, y=300)
        lbl = Label(ventana, text="PT")
        lbl.place(x=20, y=50)
        lbl1 = Label(ventana, text="LOTE")
        lbl1.place(x=20, y=100)
        lbl2 = Label(ventana, text="FECHA")
        lbl2.place(x=20, y=150)
        lbl3 = Label(ventana, text="OPERARIO")
        lbl3.place(x=20, y=200)
        lbl4 = Label(ventana, text="FECHA JULIANA")
        lbl4.place(x=320, y=50)
        lbl5 = Label(ventana, text="CONCERN")
        lbl5.place(x=620, y=50)
        lbl6 = Label(ventana, text="ALERT")
        lbl6.place(x=620, y=100)
        lbl10 = Label(ventana, text=" ")
        lbl10.place(x=450, y=250)
        lbl11 = Label(ventana, text=" ")
        lbl11.place(x=450, y=280)
        lbl12 = Label(ventana, text=" ")
        lbl12.place(x=450, y=310)
        lbl13 = Label(ventana, text=" ")
        lbl13.place(x=450, y=340)
        lbl14 = Label(ventana, text=" ")
        lbl14.place(x=750, y=250)
        lbl15 = Label(ventana, text=" ")
        lbl15.place(x=750, y=280)
        lbl16 = Label(ventana, text=" ")
        lbl16.place(x=750, y=310)
        lbl17 = Label(ventana, text="DATOS ACTUALES ETIQUETA")
        lbl17.place(x=550, y=200)
        ventana.mainloop()   #Este proceso es un loop eterno, lo q haya despues de esta instruccion no se ejecuta, o sea, crea un hilo para la ventana (para interactuar, etc) pero se lleva toda la atencion del cpu porque no tiene sleep dentro de su codigo (o si, no sé)
        print('se imprimió?')
        sleep(1)   #esto nunca se ejecuta con el mainloop de arriba

    def lectura(self):        
        global cont
        global lblCant
        
        UNIT = 0x1
        0000000000
        num = 0
        num1 = "1234567890"        
        num2 = 0
        while True:
            #read = client.read_holding_registers(2, 1, unit=UNIT) # lee la palabra 2
            #if read.registers[0]==1:
            if True:
                #if num1="999999999":   #Si la lectora lee esta etiqueta (o alguna otra que se establezca)
                #    break   #Termina la ejecucion del while, termina el hilo y sale del programa como corresponde
                if num2==0:
                    print(ope); #ss borrar
                    archivo = open ("et.prn", "w")
                    archivo.write ("^PCT~~CD,~CC^~CT~ ^XA ^MNW ^CI27 ^XZ ^XA ^MMR ^PW240 ^LL959 ^FO15,462^GB176,82,2^FS ^FO15,29^GB201,270,2^FS ^FT101,808^A@B,28,27,TT0003M_^FH\^CI28^FDOperario: " + ope + " ^FS^CI27 ^FT149,808^A@B,28,27,TT0003M_^FH\^CI28^FDFecha: 25/05/22^FS^CI27 ^FT206,489^A@I,31,31,TT0003M_^FB206,1,16,C^FH\^CI28^FD01234567^FS^CI27 ^FT56,281^A@B,31,31,TT0003M_^FH\^CI28^FD00521843050^FS^CI27 ^FT102,281^A@B,31,31,TT0003M_^FH\^CI28^FD10698^FS^CI27 ^FT148,281^A@B,31,31,TT0003M_^FH\^CI28^FD05D22^FS^CI27 ^FT194,281^A@B,31,31,TT0003M_^FH\^CI28^FD11222^FS^CI27 ^FT51,936^BQN,2,5 ^FH\^FDLA,005218430501069805D2211222^FS ^PQ1,,,Y ^XZ")
                    archivo.close ()
                    print("imprimiendo")
                    #os.system ("lp et.prn")
                if (num2==0 or num2==1):
                    num = (input ("introduzca un codigo " ))
                if num==num1: #si el codigo es correcto
                    cont=cont + 1
                       #Actualiza contador en la ventana
                    lblCant.configure(text=cont)
                    correcto="correcto " + time.strftime("%H:%M:%S ") + time.strftime("%d/%m/%y  ") + "\n" + "piezas ok " + str(cont) + "\n"
                    print (correcto)
                    archivo = open ("historico.txt", "a")
                    archivo.write ( num1 + "\n" + correcto + "\n")
                    archivo.close ()
                    #write = client.write_register(0, 1, unit=UNIT) # escribe la palabra 0 a uno para liberar
                    time.sleep(0.1)
                    num=0
                    num2=0
                    #write = client.write_register(0, 0, unit=UNIT) # escribe la palabra 0 a cero para reiniciar
                else: #si el codigo es equivocado
                    print("equivocado", time.strftime("%H:%M:%S"), time.strftime("%d/%m/%y"), "\n")
                    archivo = open ("historico.txt", "a")
                    archivo.write (num + "\n" + "equivocado" + time.strftime("%H:%M:%S ") + time.strftime("%d/%m/%y") + "\n" + "\n")
                    archivo.close ()
                    num2=1
            sleep(0.1)

if __name__ == "__main__":

       #Abrir conexion al Modbus
    #client = ModbusClient('192.168.100.156', port=502)
    #client.connect()

    Hilos = myClass()
    #ss thread = Thread(target=Hilos.grafica)
    thread2 = Thread(target=Hilos.lectura)
    #ss thread.start()
    thread2.start()
    Hilos.grafica()
    # Sin el join la ejecucion sigue su curso (imprime 'Finished') pero sin terminar el programa (hasta que terminan los hilos).
    thread2.join()
    #Con el join se bloquea la ejecucion del programa hasta que termina ese hilo.    
       #Cerrar conexion al Modbus
    #client.close()
    print('Finished')
