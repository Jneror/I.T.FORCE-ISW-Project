from Simulator import simulate
from DataCollector import DataCollector

class Option:

    def __init__(self, strike, timeMadurity, numSim, riskFreeRate, company, source):
        self.k = strike
        self.t = timeMadurity
        self.numSim = numSim
        self.r = riskFreeRate
        self.company = company
        self.source = source
        self.dc = None

    def collectData(self):
        self.dc = DataCollector(self.source, self.company, self.t * 365)
        if self.source == "Yahoo" or self.source == "Alpha":
            self.dc.getDataFromGateway()
        else:
            self.dc.getDataFromCSV()
    
    def simulateCall(self):
        self.collectData()
        return simulate(self.dc.data, self.numSim, self.t*365, self.t, self.r, self.k, "Call")
    
    def simulatePut(self):
        self.collectData()
        return simulate(self.dc.data, self.numSim, self.t*365, self.t, self.r, self.k, "Put")

#opt = Option(10, 1, 1000, 0.01, "AMD", "../AMD.csv")
