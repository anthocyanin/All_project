from tkinter import *
root = Tk()
def callback():
    print("i was used")

mb = Menubutton(root, text='click me', relief=RAISED)
mb.pack()
filemenu = Menu(mb, tearoff=False) #在mb上创建一个filemenu菜单
filemenu.add_checkbutton(label='open', command=callback, selectcolor='red')
filemenu.add_command(label='save', command=callback)
filemenu.add_separator()
filemenu.add_command(label='quit', command=root.quit)
mb.config(menu=filemenu)

mainloop()