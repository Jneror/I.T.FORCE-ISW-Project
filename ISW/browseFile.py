from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Option import Option
import matplotlib.pyplot as plt

import os

class BrowseFileScreen(BoxLayout):

    def open(self, path, filename):
        print(filename, path)
        opt = Option(10, 1, 1000, 0.01, "AMD", filename[0])
        paths, endValues, priceOff = opt.simulateCall()
        print(priceOff)
        for path in paths:
            plt.plot(path)
        plt.show()
        plt.hist(endValues, 40)
        plt.show()

    def selected(self, filename):
        print(filename)


class OptSimApp(App):
    def build(self):
        return BrowseFileScreen()

if __name__ == '__main__':
    OptSimApp().run()