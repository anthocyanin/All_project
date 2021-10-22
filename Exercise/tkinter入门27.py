from tkinter import *
root = Tk()

def callback(event):
    print("click location:", event.x, event.y)


frame = Frame(root, width=200, height=200)
frame.bind("<Button - 1>", callback)
frame.pack()

mainloop()

