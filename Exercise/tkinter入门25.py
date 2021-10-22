from tkinter import *
root = Tk()
def create():
    top = Toplevel()
    top.title("Fish")
    msg = Message(top, text="I love fish come")
    msg.pack()


Button(root, text="创建一个顶级窗口", command=create).pack()  # 主窗户上面建一个按钮，点击按钮调用create函数
mainloop()
