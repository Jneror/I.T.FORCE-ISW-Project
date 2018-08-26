from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from Option import Option
import matplotlib.pyplot as plt

import os

class FormScreen(Screen):
    
    def sim(self,strike,timeMadurity,numSim,riskFreeRate,company,source):
        opt = Option(float(strike),int(timeMadurity),int(numSim),float(riskFreeRate),company,source)
        paths, endValues, priceOff = opt.simulateCall()
        print(priceOff)
        for path in paths:
            plt.plot(path)
        plt.show()
        plt.hist(endValues, 40)
        plt.show()

class Manager(ScreenManager):
    form_screen = ObjectProperty(None)
    graphic_screen = ObjectProperty(None)

class GUIApp(App):
    def build(self):
        return Manager()

GUI = GUIApp()

GUI.run()