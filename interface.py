from tkinter import *
from YahooData import *
from simulation import *

def imprimir():
	data = load_quote(empresa.get(),fechaInicio.get(),fechaTermino.get())
	print(data)
	print(volatility(data))
	print(mean(data))


ventana = Tk()
ventana.title("Cateando")
ventana.geometry("400x400")

empresa = StringVar()
fechaInicio = StringVar()
fechaTermino = StringVar() 

empresaLabel= Label(ventana,text="Empresa").place(x=10,y=10)
empresaEntry = Entry(ventana,textvariable=empresa).place(x=120,y=10)

fechaInicioLabel= Label(ventana,text="Fecha Inicio").place(x=10,y=40)
fechaInicioEntry = Entry(ventana,textvariable=fechaInicio).place(x=120,y=40)

fechaTerminoLabel = Label(ventana,text="Fecha Termino").place(x=10,y=70)
fechaTerminoEntry = Entry(ventana,textvariable=fechaTermino).place(x=120,y=70)

boton = Button(ventana,text="Enviar",command=imprimir).place(x=10,y=100)

ventana.mainloop()