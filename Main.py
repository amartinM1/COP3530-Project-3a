import CSVReader
import Game
import Graphs
import threading
from Game import Game
from typing import List
from CSVReader import CSVReader


testGraph = Graphs.Adjlist()
is_running: bool = True

# numKeys = len(testGraph.parser.unordered_map)
# keys_1: List[str] = []
# keys_2: List[str] = []
# keys_3: List[str] = []
#
# curr_key = 1
# for key in testGraph.parser.unordered_map.keys():
#     if curr_key <= numKeys / 3:
#         keys_1.append(key)
#     elif curr_key <= 2 * (numKeys / 3):
#         keys_2.append(key)
#     else:
#         keys_3.append(key)
#     curr_key += 1
#
# t1 = threading.Thread(target=testGraph.create_subgraph, args=(keys_1,))
# t2 = threading.Thread(target=testGraph.create_subgraph, args=(keys_2,))
# t3 = threading.Thread(target=testGraph.create_subgraph, args=(keys_3,))
#
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()

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
                    if testGraph.create_minigraph(title):
                        is_searching = False
                        print(f'{testGraph.adj_list[title]}')
                    else:
                        print(f"\"{title}\" not found in Steam Store. Please search for another game:")
                else:
                    is_searching = False
                    is_running = False

        elif mode == "shortest path":
            print("Type 1 to use Dijkstra's Algorithm. Type 2 to use the Bellman-Ford Algorithm:")

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

                    testGraph.dijkstra(src, dest)

                if mode == "Bellman-Ford":
                    print("We're working on implementing Bellman-Ford. Check back soon!\n")
            else:
                is_running = False

    else:
        is_running = False

