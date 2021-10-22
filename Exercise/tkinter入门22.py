from tkinter import *
m = PanedWindow()
m.pack(fill=BOTH, expand=1)
left = Label(m, text="left pane")
m.add(left)
right = PanedWindow(orient=VERTICAL)
m.add(right)
top = Label(right, text="top pane")
right.add(top)
bottom = Label(right, text="bottom pane")
right.add(bottom)

mainloop()


