import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from Option import Option
import matplotlib.pyplot as plt

class Form(FloatLayout):
    
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