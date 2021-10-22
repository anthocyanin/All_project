from tkinter import *
from tkinter import colorchooser

root = Tk()
def callback():
    filename = colorchooser.askcolor()
    print(filename)


Button(root, text='choose color', command=callback).pack()

mainloop()

