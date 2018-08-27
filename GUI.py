from tkinter import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from Option import Option
import matplotlib.pyplot as plt

import os

def sim():
    numSim = int(n.get())
    k = float(strike.get())
    riskFreeRate = float(r.get())
    timeMadurity = float(T.get())
    sr = str(source.get())
    company = empresa.get()

    opt = Option(float(k),int(timeMadurity),int(numSim),float(riskFreeRate),company,sr)
    paths, endValues, priceOff = opt.simulateCall()
    print(priceOff)
    for path in paths:
        plt.plot(path)
    plt.show()
    plt.hist(endValues, 40)
    plt.show()

ventana = Tk()
ventana.title("Cateando")
ventana.geometry("400x300")

empresa = StringVar()
fechaInicio = StringVar()
fechaTermino = StringVar()
T = StringVar()
n = StringVar()
r = StringVar()
strike = StringVar()
source = StringVar()

empresa.set("FB")
empresaLabel= Label(ventana,text="Empresa").place(x=10,y=10)
empresaEntry = Entry(ventana,textvariable=empresa).place(x=150,y=10)

fechaInicioLabel= Label(ventana,text="Fecha Inicio").place(x=10,y=40)
fechaInicioEntry = Entry(ventana,textvariable=fechaInicio).place(x=150,y=40)

fechaTerminoLabel = Label(ventana,text="Fecha Termino").place(x=10,y=70)
fechaTerminoEntry = Entry(ventana,textvariable=fechaTermino).place(x=150,y=70)

strikeLabel = Label(ventana, text="Strike").place(x=10,y=100)
strikeEntry = Entry(ventana, textvariable=strike).place(x=150,y=100)

TLabel = Label(ventana, text="Tiempo de Maduracion").place(x=10,y=130)
TEntry = Entry(ventana, textvariable=T).place(x=150,y=130)

nLabel = Label(ventana, text="Numero de simulaciones").place(x=10,y=160)
nEntry = Entry(ventana, textvariable=n).place(x=150,y=160)

rLabel = Label(ventana, text="r").place(x=10,y=190)
rEntry = Entry(ventana, textvariable=r).place(x=150,y=190)

sourceLabel = Label(ventana,text="Source").place(x=10,y=220)
sourceOption = Entry(ventana,textvariable=source).place(x=150, y = 215)

boton = Button(ventana,text="Enviar",command=sim).place(x=10,y=250)

ventana.mainloop()