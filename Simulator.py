import numpy as np
from alpha_vantage.timeseries import TimeSeries

def volatility(data):
    n = len(data)-1
    logaritmos = np.zeros(n)
    for i in range(n):
        print(data[i+1], data[i])
        logaritmos[i] = np.log(data[i+1]/data[i])
    return np.std(logaritmos, dtype=np.float64)

def simulate(data, numSim, numIt, t, r, k, type):
    dt = t/numIt
    v = volatility(data['Close'])
    s0 = data['Close'].iloc[0]
    print("Simulating:", dt, v, s0)
    brownian = np.exp((r - 0.5*v**2)*dt + v*np.random.normal(0, dt, (numSim, numIt)))
    paths = s0 * np.cumprod(brownian,1)
    endValues = paths[:,-1]
    if type == "Call":
        return (paths, endValues, np.mean((np.max(endValues-k, 0))*np.exp(-r*t)))
    else:
        return (paths, endValues, np.mean((np.max(k - endValues, 0))*np.exp(-r*t)))