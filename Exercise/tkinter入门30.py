from tkinter import *

root = Tk()
Label(root, text="user name").grid(row=0, sticky=W)
Label(root, text="password").grid(row=1, sticky=W)

Entry(root).grid(row=0, column=1)
Entry(root, show='*').grid(row=1, column=1)
Label(root, text="this place is used for \nwriting your name and password").grid(row=0, column=2, rowspan=2, padx=5, pady=5)
Button(text="submit", width=10).grid(row=2, columnspan=3, pady=5)

mainloop()

