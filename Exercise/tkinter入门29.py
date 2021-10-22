from tkinter import *
root = Tk()

def callback(event):
    print("click location:", event.x, event.y)


frame = Frame(root, width=200, height=200)
frame.bind("<Motion>", callback)  # 在这个框架里 绑定了Motion事件，每次触发这个事件则调用callback函数
frame.pack()

mainloop()

