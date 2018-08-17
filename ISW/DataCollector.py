from Gateway import gateway as gw
import pandas as pd

class DataCollector:

    def __init__(self, dataSource, company, numDays):
        self.dataSource = dataSource
        self.data = None
        self.company = company
        self.numDays = numDays
    
    def getDataFromGateway(self):
        if self.dataSource == "Yahoo":
            self.data = gw.getDailyDataFromYahoo(self.company, self.numDays)
        elif self.dataSource == "Alpha":
            self.data = gw.getDailyDataFromAlpha(self.company, self.numDays)
    
    def getDataFromCSV(self):
        df = pd.read_csv(self.dataSource)[-1-self.numDays: -1]
        df = df.set_index('Date')
        self.data = df.drop(columns=['Adj Close'])
    
    def haveData(self):
        if (self.data != None):
            return True
        return False


#dataCollector = DataCollector("AlphaVantage", "AMD", 100)
#dataCollector.getDataFromGateway()
#print(dataCollector.data)

#dc = DataCollector("../AMD.csv", "AMD", 100)
#data = dc.getDataFromCSV()
#print(data)