import CSVReader
import Game
import Graphs
from Game import Game
from CSVReader import CSVReader


testGraph = Graphs.Adjlist()
is_running: bool = True

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

                    testGraph.disjktra(src, dest)

                if mode == "Bellman-Ford":
                    print("We're working on implementing Bellman-Ford. Check back soon!\n")
            else:
                is_running = False

    else:
        is_running = False

