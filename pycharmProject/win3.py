#! usr/bin/python3

from gpiozero import MCP3008
from tkinter import Tk
from threading import Timer

class LM35App:
    def __init__(self):
        print("LM35App的實體被建立")
        self.lm35 = MCP3008(channel=6)
        self.checkTemperature()

    def checkTemperature(self):
        print(self.lm35.value * 3.3 * 100)
        Timer(1, self.checkTemperature()).start()


if __name__ == "__main__":
    window = Tk()
    window.title("LM35")
    app = LM35App()
    window.mainloop()
