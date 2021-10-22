from tkinter import *
root = Tk()

def callback():
    print("l was used")
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='open', command=callback)
filemenu.add_command(label='save', command=callback)
filemenu.add_separator() #创建一条分割线
filemenu.add_command(label='quit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label="ctrx", command=callback)
editmenu.add_command(label='ctrc', command=callback)
editmenu.add_command(label='ctrv', command=callback)
menubar.add_cascade(label='Edit', menu=editmenu)

root.config(menu=menubar)

mainloop()



