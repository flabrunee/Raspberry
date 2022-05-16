#!/usr/bin/env python3
#import tkinter as tk
#root = tk.Tk()
#root.mainloop()
import time
from tkinter import *

ventana = Tk()
ventana.title("CARGAR DATOS ETIQUETAS")
ventana.geometry('800x600')
#lbl = Label(ventana, text="Hello")
#lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(ventana, text="GUARDAR")
#btn = Button(ventana, text="ACEPTAR", command=cliked)
#btn.grid(column=1, row=0)
btn.place(x=300,y=450)

#crear etiqueta en la ventana, hay tres opciones para trabajar con el posicionamieno "pack, grid, place"
lbl=Label(ventana, text="OPERARIO")
lbl.place(x=10,y=25)
lbl1=Label(ventana, text="LOTE")
lbl1.place(x=10,y=75)
lbl2=Label(ventana, text="FECHA")
lbl2.place(x=10,y=125)
lbl3=Label(ventana, text="CODIGO")
lbl3.place(x=10,y=175)



#definir variable para campos
text_ope=StringVar()
text_lote=StringVar()
#text_fecha=StringVar()
text_fecha= time.strftime("%d/%m/%y  ")
ver_ope=StringVar()
#time = StringVar()

#definir campos escritura variables
cpo1=Entry(ventana,font=('arial',15,'bold'),width=10,textvariable=text_ope,bd=5,insertwidth=4,bg="powder blue",justify="right").place(x=120,y=20)
cpo2=Entry(ventana,font=('arial',15,'bold'),width=10,textvariable=text_lote,bd=5,insertwidth=4,bg="powder blue",justify="right").place(x=120,y=70)
cpo3=Entry(ventana,font=('arial',15,'bold'),width=10,textvariable=text_fecha,bd=5,insertwidth=4,bg="powder blue",justify="right").place(x=120,y=120)
cpo4=Entry(ventana,font=('arial',15,'bold'),width=30,textvariable=ver_ope,bd=5,insertwidth=4,bg="powder blue",justify="right").place(x=120,y=170)

ventana.mainloop()
