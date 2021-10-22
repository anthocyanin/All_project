from tkinter import *

root = Tk()
LANGS = [("python", 1), ("perl", 2), ("rudy", 3), ("lua", 4)]
v = IntVar()
v.set(1)
for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()


