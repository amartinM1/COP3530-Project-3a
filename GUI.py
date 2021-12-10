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
    global Dijkstras
    global Dijkstras_edge
    if clicked.get() == "Search":
        search = True
        Dijkstras = False
        Dijkstras_edge = False
        text.insert(tk.END, "Enter a game into the search bar to see the top 10 closest matches")
    elif clicked.get() == "Dijkstra's":
        search = False
        Dijkstras = True
        Dijkstras_edge = False
        text.insert(tk.END, "To run Dijkstra's algorithm, please search two games separated by a comma in the form of "
                            "source, destination")
    elif clicked.get() == "Dijkstra's with edge list":
        search = False
        Dijkstras = False
        Dijkstras_edge = True
        text.insert(tk.END, "To run Dijkstra's algorithm for an edge list, please search two games separated by a "
                            "comma in the form of source, destination")


def find():
    text.delete('1.0', END)
    global search
    global Dijkstras
    global Dijkstras_edge
    a_file = open("full_graph1.pkl", "rb")
    full_graph = Graphs.Adjlist()
    full_graph.adj_list = pickle.load(a_file)
    a_file.close()
    if search is True:
        global searched_game
        searched_title = modify.get()
        if searched_title in reader.unordered_map.keys():
            top_games: list
            top_games = full_graph.adj_list[searched_title]
            for edge in top_games:
                text.insert(tk.END, edge[1] + "  [weight = ")
                text.insert(tk.END, edge[0])
                text.insert(tk.END, ']\n\n')
        else:
            text.insert(tk.END, "Error: Game not found in our database. Make sure that your search matches the game "
                                "title exactly")
    elif Dijkstras is True:
        searched_titles: str
        searched_titles_split: list
        searched_titles = modify.get()
        searched_titles_split = searched_titles.split(', ')
        string_list = full_graph.dijkstra(searched_titles_split[0], searched_titles_split[1])
        if "No possible path" in string_list or "Unsuccessful" == string_list:
            text.insert(tk.END, string_list)
        else:
            for string in string_list:
                text.insert(tk.END, string)
                text.insert(tk.END, '\n\n')
    elif Dijkstras_edge is True:
        searched_titles: str
        searched_titles_split: list
        searched_titles = modify.get()
        searched_titles_split = searched_titles.split(', ')
        string_list = full_graph.dijkstra_edge_list(searched_titles_split[0], searched_titles_split[1])
        if "No possible path" in string_list or "Unsuccessful" == string_list:
            text.insert(tk.END, string_list)
        else:
            for string in string_list:
                text.insert(tk.END, string)
                text.insert(tk.END, '\n\n')


search = True
Dijkstras = False
Dijkstras_edge = False
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
    "Dijkstra's with adjacency list", "Dijkstra's with edge list", "Search"
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
