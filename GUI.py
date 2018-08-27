from tkinter import *
from tkinter.filedialog import askopenfilename
from Option import Option
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import os

def fileChooser():
    filename = askopenfilename()
    source.set(filename)
    return

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
    
    f = Figure(figsize=(6,2.8), dpi = 80)
    a = f.add_subplot(111)
    for path in paths:
        a.plot(path)
    a.set(xlabel = "Iteración", ylabel = "priceOff", title = "Cambio del precio en distintas simulaciones")
    a.grid()


    f2 = Figure(figsize=(6,2.8), dpi = 80)
    b = f2.add_subplot(111)
    for path in paths:
        b.hist(endValues, 40)
    b.set(title = "Histograma precio final")
    b.grid()

    ventana.geometry("950x450")
    canvas = FigureCanvasTkAgg(f, ventana)
    canvas.show()
    canvas.get_tk_widget().place(x=350,y=10)

    canvas2 = FigureCanvasTkAgg(f2, ventana)
    canvas2.show()
    canvas2.get_tk_widget().place(x=350,y=210)

    result = Label(ventana, text= "el valor de la opción es: " + str(priceOff)).place(x=10,y=310)

ventana = Tk()
ventana.title("Cateando")
ventana.geometry("500x350")


empresa = StringVar()
T = StringVar()
n = StringVar()
r = StringVar()
strike = StringVar()
source = StringVar()

empresa.set("FB")
strike.set("100")
T.set("1")
n.set("100")
r.set("0.01")
source.set("Alpha")
empresaLabel= Label(ventana,text="Empresa").place(x=10,y=10)
empresaEntry = Entry(ventana,textvariable=empresa).place(x=150,y=10)

strikeLabel = Label(ventana, text="Strike").place(x=10,y=50)
strikeEntry = Entry(ventana, textvariable=strike).place(x=150,y=50)

TLabel = Label(ventana, text="Tiempo de Maduracion").place(x=10,y=90)
TEntry = Entry(ventana, textvariable=T).place(x=150,y=90)

nLabel = Label(ventana, text="Numero de simulaciones").place(x=10,y=130)
nEntry = Entry(ventana, textvariable=n).place(x=150,y=130)

rLabel = Label(ventana, text="r").place(x=10,y=170)
rEntry = Entry(ventana, textvariable=r).place(x=150,y=170)

sourceLabel = Label(ventana,text="Source").place(x=10,y=210)
sourceOption = Entry(ventana,textvariable=source).place(x=150, y = 210)

boton = Button(ventana,text="Buscar csv",command=fileChooser).place(x=10,y=240)

boton = Button(ventana,text="Enviar",command=sim).place(x=10,y=280)

ventana.mainloop()