from tkinter import *

def openLight():
    print("openLight")

def closeLight():
    print("close Light")

if __name__ == "__main__":
    window = Tk()
    window.title("led control")
    openButton = Button(window, text="開燈", command=openLight, padx = 10, pady = 10)
    openButton.pack(side=LEFT)

    closeButton = Button(window, text="關燈", command=closeLight, padx=10, pady=10)
    closeButton.pack(side=LEFT)

    window.mainloop()
