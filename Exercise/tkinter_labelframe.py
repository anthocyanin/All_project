from tkinter import *

root = Tk()
group = LabelFrame(root, text="最好的语言是？", padx=5, pady=10)
group.pack(padx=10, pady=10)
LANGS = [("python", 1), ("perl", 2), ("rudy", 3), ("lua", 4)]
v = IntVar()
v.set(1)
for lang, num in LANGS:
    b = Radiobutton(group, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()
