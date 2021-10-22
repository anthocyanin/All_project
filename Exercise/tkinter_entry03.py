from tkinter import *

root = Tk()
Label(root, text="账号：").grid(row=0)
Label(root, text="密码：").grid(row=1)
v1 = StringVar()
v2 = StringVar()
e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=v2, show="*")
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)

def show():
    e1.insert(0, "小甲鱼")
    e2.insert(0, "fishc.com")
    print("账号：%s" % v1.get())
    print("密码：%s" % v2.get())
Button(root, text="click", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(root, text="quit", width=10,command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()


