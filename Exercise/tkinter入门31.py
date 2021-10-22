# 使用place可以将子组件显示在父组件的正中间
from tkinter import *
root = Tk()
def callback():
    print("正中靶心")


Button(root, text="click me", command=callback).place(relx=0.5, rely=0.5, anchor=CENTER)

mainloop()
