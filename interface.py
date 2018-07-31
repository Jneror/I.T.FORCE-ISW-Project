from tkinter import *
from YahooData import *
from simulation import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

def calculate():
	data = load_quote(empresa.get(),fechaInicio.get(),fechaTermino.get())
	sigma = volatility(data)
	N = int(n.get())
	S0 = data[0][4]
	k = float(strike.get())
	R = float(r.get())
	Tm = float(T.get())
	call = str(callOrPut.get())
	print(call)
	if (call == "Call"):
		prices = monte_carlo(N,S0,k,R,sigma,Tm, True)
	else:
		prices = monte_carlo(N,S0,k,R,sigma,Tm, False)
	mc = np.mean(prices)

	f = Figure(figsize=(7,5), dpi = 80)
	a = f.add_subplot(111)
	a.plot(prices, color="red")
	a.set(xlabel = "Iteración", ylabel = "priceOff", title = "Cambio del precio en distintas simulaciones")
	a.grid()

	ventana.geometry("950x450")
	canvas = FigureCanvasTkAgg(f, ventana)
	canvas.show()
	canvas.get_tk_widget().place(x=350,y=10)

	result = Label(ventana, text= "el valor de la opción es: " + str(mc)).place(x=10,y=300)



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
callOrPut = StringVar(ventana)
callOrPut.set("Call")

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

callOrPutLabel = Label(ventana,text="Call or put").place(x=10,y=220)
callOrPutOption = OptionMenu(ventana, callOrPut, "Call", "Put").place(x=150, y = 215)

boton = Button(ventana,text="Enviar",command=calculate).place(x=10,y=250)

ventana.mainloop()