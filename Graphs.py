import CSVReader
import Game
import heapq


class Adjlist:
    #  calls reader to populate dictionary
    parser = CSVReader.CSVReader("steam.csv")
    parser.read_file()

    # constructor
    def __init__(self, _dict={}, _count=0, fro='', to=''):
        self.dict = _dict
        self.count = _count
        self.fro = fro
        self.to = to

    def create_graph(self):
        #  iterate through each game in the unordered_map
        for key in self.parser.unordered_map.keys():
            this_game =  self.parser.unordered_map[key] # dictionary value isn't immediately translated to Game() object

            relevant_games = {}
            # loop through the steamspy_tags of the game and create a dictionary (relevant_games) that has the union
            # of all the steamspy tags
            for tag in this_game.steamspy_tags:
                for curr_title in self.parser.tags_map[tag]:
                    weight = 1

                    if curr_title not in relevant_games:
                        weight += self.calculate_weight(this_game, curr_title, weight)
                        relevant_games[curr_title] = weight

                    if curr_title in relevant_games:
                        relevant_games[curr_title] = relevant_games[curr_title] + 1

        # loop through the steamspy_tags of the game and create a set that has the union of all the steamspy tags
        # loop through the union set and at each game, calculate the similarity score and push it into a heapq (
        # minheap) of tuples (tuples being name, weight) if the heapq (minheap) has more than k elements, delete the
        # largest element push the finished heapq into a dicitonary of heapqs with the game title as key
        # reccomendations[title] = heapq

    def calculate_weight(self, this_game, curr_title: str, initial_weight):
        weight = 0
        comparison = self.parser.unordered_map[curr_title]

        #  compare categories
        game_numcats = len(this_game.categories)
        comparison_numcats = len(comparison.categories)

        if game_numcats > comparison_numcats:
            for category in this_game.categories:
                if category in comparison.categories:
                    weight += 1
                else:
                    weight -= 1

        else:
            for category in comparison.categories:
                if category in this_game.categories:
                    weight += 1
                else:
                    weight -= 1

        #  compare genres

        #  compare English support

        #  compare platforms

        # check for initial_weight + weight <= 0

        return weight
