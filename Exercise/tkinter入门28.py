from tkinter import *
root = Tk()

def callback(event):
    print("click loaction:", repr(event.char))


frame = Frame(root, width=200, height=200)
frame.bind("<Key>", callback)  # 绑定键盘事件
frame.focus_set()  # 获的焦点
frame.pack()

mainloop()



