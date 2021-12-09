import pickle
import tkinter as tk
import Game
import CSVReader
from tkinter import *

import Graphs


def show():
    text.delete('1.0', END)
    label.config(text=clicked.get())
    global search
    global Dikstras
    global Bellman_Ford
    if clicked.get() == "Search":
        search = True
        Dikstras = False
        Bellman_Ford = False
        text.insert(tk.END, "Enter a game into the search bar to see the top 10 closest matches")
    elif clicked.get() == "Dikstra's":
        search = False
        Dikstras = True
        Bellman_Ford = False
        text.insert(tk.END, "To run Dikstra's algorithm, please search two games separated by a comma")
    elif clicked.get() == "Bellman-Ford":
        search = False
        Dikstras = False
        Bellman_Ford = True
        text.insert(tk.END, "To run Bellman-Ford's algorithm, please search two games separated by a comma")


def find():
    text.delete('1.0', END)
    global search
    global Dikstras
    global Bellman_Ford
    if search is True:
        global searched_game
        searched_title = modify.get()

        a_file = open("full_graph1.pkl", "rb")
        full_graph = Graphs.Adjlist()
        full_graph.adj_list = pickle.load(a_file)
        a_file.close()

        print(full_graph.adj_list[searched_title])

        top_games: list
        top_games = full_graph.adj_list[searched_title]
        for edge in top_games:
            text.insert(tk.END, edge[1] + "  [weight = ")
            text.insert(tk.END, edge[0])
            text.insert(tk.END, ']\n\n')
    elif Dikstras is True:
        text.insert(tk.END, "Running Dikstra's Algorithm")
    elif Bellman_Ford is True:
        text.insert(tk.END, "Running Bellman-Ford's Algorithm")
    # elif Bellman_Ford is True


search = True
Dikstras = False
Bellman_Ford = False
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
Frm.pack(side=LEFT)
# Dropdown menu options
options = [
    "Dikstra's", "Bellman-Ford", "Search"
]
# datatype of menu text
clicked = StringVar()
clicked.set("Mode")
# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
label = Label(root, text=" ")

# Calls Reader
reader = CSVReader.CSVReader("steam.csv")
reader.read_file()
searched_game = Game.Game()
text = Text(canvas, height=40, width=140, yscrollcommand=True, bg="#263D42", fg="white")
text.pack()
button2 = Button(root, text="Enter", command=show).pack(side=RIGHT)
drop.pack(side=RIGHT)
button.config(command=find)
root.mainloop()
