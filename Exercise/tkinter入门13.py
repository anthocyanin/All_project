from tkinter import *
root =Tk()
def callback():
    print("i was used")
menu = Menu(root, tearoff=True)
menu.add_command(label="year", command=callback)
menu.add_command(label="review", command=callback)
frame = Frame(root, width=512, height=512)
frame.pack()
def popup(event):
    menu.post(event.x_root, event.y_root)

frame.bind('<Button - 3>', popup)

mainloop()
