import CSVReader
import Game
import Graphs
import pickle
import threading
from Game import Game
from typing import List
from CSVReader import CSVReader



is_running: bool = True
a_file = open("full_graph1.pkl", "rb")
full_graph = Graphs.Adjlist()
full_graph.adj_list = pickle.load(a_file)
a_file.close()

# full_graph.create_graph()
# a_file = open("full_graph1.pkl", "wb")
# pickle.dump(full_graph.adj_list, a_file)
# a_file.close()

print("Welcome to QuestSeeker!")
mode: str = ""

while is_running:
    print("\nType 1 to find recommendations for a game, or 2 to find the shortest path between two games:")
    print("Alternatively, type \"quit\" at any time to quit")

    response = input()

    if response == "1":
        mode = "lookup"

    elif response == "2":
        mode = "shortest path"

    if response != "quit":
        if mode == "lookup":  # everything here checked for bugs. Works perfectly
            is_searching = True
            print("Please search a game, or type \"quit\" to quit:")
            while is_searching:
                title = input()

                if title != "quit":
                    if title in full_graph.adj_list.keys():
                        print(f'{full_graph.adj_list[title]}')
                        is_searching = False
                    else:
                        print(f"\"{title}\" not found in Steam Store. Please search for another game:")
                else:
                    is_searching = False
                    is_running = False

        elif mode == "shortest path":
            print("Type 1 to use Dijkstra's Algorithm via Adjacency List. Type 2 to use Dijkstra's Algorithm via Edge List:")

            response = input()

            if response == "1":
                mode = "Dijkstra"

            elif response == "2":
                mode = "Bellman-Ford"

            if response != "quit":
                if mode == "Dijkstra":
                    print("Please input source game:")

                    response = input()
                    src: str = response

                    if response == "quit":
                        is_searching = False
                        break

                    print("Please input destination game:")

                    if response == "quit":
                        is_searching = False
                        break

                    response: str = input()
                    dest: str = response

                    full_graph.dijkstra(src, dest)

                if mode == "Bellman-Ford":
                    print("Please input source game:")

                    response = input()
                    src: str = response

                    if response == "quit":
                        is_searching = False
                        break

                    print("Please input destination game:")

                    if response == "quit":
                        is_searching = False
                        break

                    response: str = input()
                    dest: str = response

                    full_graph.dijkstra_edge_list(src, dest)
            else:
                is_running = False

    else:
        is_running = False
