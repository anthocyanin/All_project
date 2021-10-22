from tkinter import *
root = Tk()
w = Canvas(root, width=200, height=100)
w.pack()
w.create_line(0, 0, 200, 100, fill='green', width=3)
w.create_line(200, 0, 0, 100, fill='green', width=3)
w.create_rectangle(40, 20, 160, 80, fill='green', dash=(4, 4))
w.create_oval(40, 20, 160, 80, fill='pink') #画一个椭圆
w.create_oval(70, 20, 130, 80, fill='blue') #画一个圆
w.create_text(100, 50, text='fish cat love') #在100，50，这个点开始写，往两边扩散
mainloop()