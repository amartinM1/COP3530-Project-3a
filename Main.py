import CSVReader
import Game
import Graphs
from Game import Game
from CSVReader import CSVReader


testGraph = Graphs.Adjlist()


print("Hello! Please search a game:")
title = input()
testGraph.create_minigraph(title)
print(testGraph.adj_list[title])
