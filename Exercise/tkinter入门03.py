from tkinter import *
root = Tk()
text = Text(root, width=30, height=5, undo=True) #开启撤销功能
text.pack()
text.insert(INSERT, "i love fish come")
def show():
    text.edit_undo()
Button(root, text="撤销", command=show).pack() #点击撤销命令，执行恢复函数

mainloop()