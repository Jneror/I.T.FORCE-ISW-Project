import numpy as np

def monte_carlo(n,S0,K,r,sigma,T):
	m = 1000
	dt = T/m
	suma = 0
	for i in range(n):
		S = S0
		for j in range(m):
			S = S*np.exp((r-0.5*sigma**2)*dt+sigma*W)
		suma = suma + np.exp(-r*T)*max(S-K,0)
	value = suma/n
	return value