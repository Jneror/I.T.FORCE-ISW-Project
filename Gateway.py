import YahooData as yd
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from pandas.tseries.offsets import BDay
import numpy as np

class Gateway:

    dataColumns = np.array(["Open", "High", "Low", "Close", "Volume"])

    def activeDays(numDays):
        numActiveDays = 0
        while (numDays > 365):
            numActiveDays += 251

    def yahooDateFormat(self, date):
        date = str(date)
        return "{}{}{}".format(date[0:4], date[5:7], date[8:10])

    def getDailyDataFromYahoo(self, company, numDays):
        now = self.yahooDateFormat(pd.datetime.today())
        n_days_ago = self.yahooDateFormat(pd.datetime.today()-BDay(int(numDays*1.1)) )
        rawData = yd.load_yahoo_quote(company, n_days_ago, now)[:numDays+1]
        data = [i.split(',') for i in rawData]
        for i in range(1, numDays+1):
            data[i] = [data[i][0],] + list(map(lambda x: float(x), data[i][1:]))
        df = pd.DataFrame(data = data[1:][:], columns = data[0])
        df = df.set_index("Date")
        df = df.drop(columns=['Adj Close'])
        return df
    
    def getDailyDataFromAlpha(self, company, numDays):
        print(company, numDays)
        ts = TimeSeries(key='7ERSLTME9P4Q0F6V', output_format = 'pandas')
        if numDays < 100:
            df = ts.get_daily(symbol=company, outputsize='compact')[0][-1-numDays:-1]
        else:
            df = ts.get_daily(symbol=company, outputsize='full')[0][-1-numDays:-1]
        df.columns = self.dataColumns
        return df

gateway = Gateway()