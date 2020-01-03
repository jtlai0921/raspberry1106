#! usr/bin/python3

from gpiozero import MCP3008
from tkinter import *
from threading import Timer

class LM35App:
    def __init__(self,window):
        print("LM35App的實體被建立")
        self.vrText = StringVar()
        mainFrame = Frame(window, borderwidth=2, relief=GROOVE)
        Label(mainFrame, text="溫度:").pack(side=LEFT)
        Entry(mainFrame, width=20, state=DISABLED, textvariable=self.vrText).pack(side=LEFT)
        mainFrame.pack(padx=30, pady=30)
        self.lm35 = MCP3008(channel=6)
        self.checkTemperature()

    def checkTemperature(self):

        self.vrText.set(str(self.lm35.value * 3.3 * 100))
        Timer(1, self.checkTemperature).start()


if __name__ == "__main__":
    window = Tk()
    window.title("LM35")
    app = LM35App(window)
    window.mainloop()
