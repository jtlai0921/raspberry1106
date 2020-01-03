#! usr/bin/python3

from gpiozero import MCP3008
from tkinter import Tk
from time import sleep

'''
while True:
    lm35 = MCP3008(channel=6)
    print(lm35.value * 3.3 * 100)
    sleep(1)
'''
class LM35App:
    def __init__(self):
        print("LM35App的實體被建立")

if __name__ == "__main__":
    window = Tk()
    window.title("LM35")
    app = LM35App()
    window.mainloop()
