import CSVReader
import Game
from Game import Game
from CSVReader import CSVReader


def game_info(title):
    if title in reader.unorderedMap:
        game = reader.unorderedMap[title]
        game.print()

        tags = game.get_tags()
        print(f'\nTags:')
        for tag in tags:
            print(f'{tag}: {reader.tags_map[tag]}')


reader = CSVReader("steam.csv")
reader.read_file()

print("Hello! Please search a game:")
title = input()
game_info(title)
