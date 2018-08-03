import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
import sys

def volatility(data):
    logaritmos = np.zeros(len(data)-1)
    for i in range(len(data)-1):
        logaritmos[i] = np.log(data[i+1][4]/data[i][4])
    return np.std(logaritmos, dtype=np.float64)

def mean(data):
    sum = 0.0
    for i in range(len(data)):
        sum = sum + data[i][4]
    return sum/len(data)

def monte_carlo_v0(n,S0,K,r,sigma,T):
	m = 1000
	dt = T/m
	suma = 0
	for i in range(n):
		S = S0
		for j in range(m):
			W = np.random.normal(0,dt)
			S = S*np.exp((r-0.5*sigma**2)*dt+sigma*W)
		suma = suma + np.exp(-r*T)*max(S-K,0)
	value = suma/n
	return value

def monte_carlo(n, S0, K, r, sigma, T, call):
	m = 1000
	dt = float(T)/m
	prices = np.zeros(n)
	for i in range(n):
		S = S0
		for j in range(m):
			W = np.random.normal(0,dt)
			S = S*np.exp((r-0.5*sigma**2)*dt+sigma*W)
		if (call):
			prices[i] += np.exp(-r*T)*max(S - K,0)
		else:
			prices[i] += np.exp(-r*T)*max(K - S,0)
	return prices
    
def calculate():
    sigma = volatility(data)
    S0 = data[0][4]
    if (call == "Call"):
        prices = monte_carlo(N,S0,k,R,sigma,Tm, True)
    else:
        prices = monte_carlo(N,S0,k,R,sigma,Tm, False)
    return np.mean(prices)

Tm = float(sys.argv[1])
N = int(sys.argv[2])
R = float(sys.argv[3])
k = float(sys.argv[4])
call = str(sys.argv[5])
data = str(sys.argv[6])

result = {"promedio": calculate()}
print(str(result))
sys.stdout.flush()