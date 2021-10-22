from tkinter import *
root = Tk()
def callback():
    print('i was used')

#创建一个顶级菜单
menubar = Menu(root)
#创建checkbutton 关联变量
openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()
#创建一个下拉菜单'File'，并把它添加到顶级菜单中
filemenu = Menu(menubar, tearoff=True)
filemenu.add_checkbutton(label="open", command=callback, variable=openVar)
filemenu.add_checkbutton(label='save', command=callback, variable=saveVar)
filemenu.add_separator()
filemenu.add_checkbutton(label='quit', command=root.quit, variable=quitVar)
menubar.add_cascade(label='File', menu=filemenu)
#创建radiobutton 关联变量
editVar = IntVar()
editVar.set(1)
#创建另一个下拉菜单'Edit'，并把它添加到顶级菜单中
editmenu = Menu(menubar, tearoff=True)
editmenu.add_radiobutton(label='cut', command=callback, variable=editVar, value=1)
editmenu.add_radiobutton(label='copy', command=callback, variable=editVar, value=2)
editmenu.add_radiobutton(label='paste', command=callback, variable=editVar, value=3)
menubar.add_cascade(label='Edit', menu=editmenu)

root.config(menu=menubar)
mainloop()



