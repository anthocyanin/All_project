from tkinter import *
def callback():
    var.set("吹吧，我才不信呢")

root  = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
#创建一个label对象
var = StringVar()
var.set("你所下载的内容含有未成年人限制信息，\n请满18周岁后再看")
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack(side=LEFT)
#创建一个图像标签对象
#用PhotoImage实例话一个图片对象
photo = PhotoImage("Macintosh HD\\Users\\gonghuidepro\\Desktop\\工作文件\\营销部门\\WechatIMG9.png")
imgLabel = Label(frame1, image=photo)
imgLabel.pack(side=RIGHT)
#加一个按钮
theButton = Button(frame2, text="已满十八周岁", command=callback)
theButton.pack()
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()

