import tkinter as tk
from tkinter import *
# Main GUI object
root = tk.Tk()
Frm = Frame(root)
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack(side=BOTTOM)
# Search bar code
Label(Frm, text='Search:').pack(side=LEFT)
modify = Entry(Frm)
modify.pack(side=LEFT, fill=BOTH, expand=1)
modify.focus_set()
button = Button(Frm, text='Enter')
button.pack(side=RIGHT)
Frm.pack(side=TOP)
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
# datatype of menu text
clicked = StringVar()
clicked.set("Filter")
# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
label = Label(root, text=" ")


def show():
    label.config(text=clicked.get())
    print(clicked.get())


def find():
    print(modify.get())


button2 = Button(root, text="Enter", command=show).pack(side=RIGHT)
drop.pack(side=RIGHT)
button.config(command=find)
root.mainloop()
