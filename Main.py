import CSVReader
import Game
import Graphs
from Game import Game
from CSVReader import CSVReader


def game_info(title):
    if title in reader.unordered_map:
        game = reader.unordered_map[title]
        game.print()

        tags = game.get_tags()
        print(f'\nTags:')
        for tag in tags:
            print(f'{tag}: {reader.tags_map[tag]}')



testGraph = Graphs.Adjlist()
testGraph.create_graph()

reader = CSVReader("steam.csv")
reader.read_file()

g = reader.unordered_map["Call of Duty"]
print(g.name)

print("Hello! Please search a game:")
title = input()
game_info(title)
