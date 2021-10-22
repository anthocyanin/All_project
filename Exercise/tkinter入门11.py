from tkinter import *

root = Tk()
def callback():
    print("我被调用了")
menubar = Menu(root)
menubar.add_command(label="Hello", command=callback)
menubar.add_command(label="Quit", command=root.quit)
root.config(menu=menubar)

root.mainloop()