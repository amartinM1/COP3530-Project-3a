import tkinter as tk
from tkinter import *
root = tk.Tk()
Frm = Frame(root)
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack(side=BOTTOM)
Label(Frm, text='Search:').pack(side=LEFT)
modify = Entry(Frm)
modify.pack(side=LEFT, fill=BOTH, expand=1)
modify.focus_set()
button = Button(Frm, text='Enter')
button.pack(side=RIGHT)
Frm.pack(side=TOP)


def find():
    print(modify.get())


button.config(command=find)
root.mainloop()


