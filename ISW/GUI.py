from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from Option import Option
import matplotlib.pyplot as plt

import os

class Form(AnchorLayout):
    
    def sim(self,strike,timeMadurity,numSim,riskFreeRate,company,source):
        opt = Option(float(strike),int(timeMadurity),int(numSim),float(riskFreeRate),company,source)
        paths, endValues, priceOff = opt.simulateCall()
        print(priceOff)
        for path in paths:
            plt.plot(path)
        plt.show()
        plt.hist(endValues, 40)
        plt.show()

class GUIApp(App):
    def build(self):
        return Form()

GUI = GUIApp()

GUI.run()