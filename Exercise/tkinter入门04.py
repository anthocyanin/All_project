from tkinter import *
root = Tk()
text = Text(root, width=30, height=5, autoseparators=False, undo=True, maxundo=10) #把tkinter默认的自动分隔关闭，开启撤销功能
text.pack()

def callback(event):
    text.edit_separator()
text.bind('<Key>', callback) #绑定键盘事件，键盘输入一次，算一次事件，调用一次callback函数，callback函数输入一次分隔符
text.insert(INSERT, "i love fish come")
def show():
    text.edit_undo()
Button(root, text="撤销", command=show).pack() #每次撤销只撤销一个输入

mainloop()