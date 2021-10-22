from tkinter import *
root = Tk()

variable = StringVar()
variable.set('one')
#在root主窗户创建一个选项菜单组件
w = OptionMenu(root, variable, 'one', 'two', 'three')
w.pack()

def callback():
    print(variable.get())


Button(root, text='click me', command=callback).pack()


mainloop()
