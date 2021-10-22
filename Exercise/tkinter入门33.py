from tkinter import *
from tkinter import filedialog
root = Tk()
def callback():
    fileName = filedialog.askopenfilename()
    print(fileName)


Button(root, text="open file", command=callback).pack()

mainloop()
