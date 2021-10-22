from tkinter import *
root = Tk()
w1 = Message(root, text='这是一则消息', width=100)  # 可见message是label的变体
w1.pack()
w2 = Message(root, text='苹果在2006年10月24日发布了使用Intel Core 2 Duo处理器的MacBook Pro笔记本电脑', width=100)
w2.pack()
mainloop()
