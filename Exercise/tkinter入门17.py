from tkinter import *
OPTIONS = [
    'California',
    '458',
    'FF',
    'enzo',
    'LaFerrari'
]
root = Tk()
variable = StringVar()
variable.set(OPTIONS[0])
w = OptionMenu(root, variable, *OPTIONS)
w.pack()

def callback():
    print(variable.get())


Button(root, text='click me', command=callback).pack()

mainloop()
