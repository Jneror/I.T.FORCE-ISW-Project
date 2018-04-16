import numpy as np

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

def monte_carlo(n,S0,K,r,sigma,T):
	m = 1000
	dt = T/m
	suma = 0
	W = np.random.normal(0,dt,1000)
	for i in range(n):
		S = S0
		for j in range(m):
			S = S*np.exp((r-0.5*sigma**2)*dt+sigma*W)
		suma = suma + np.exp(-r*T)*max(S-K,0)
	value = suma/n
	return value