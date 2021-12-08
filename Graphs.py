import CSVReader
import Game
import heapq
from typing import Dict


class Adjlist:
    #  calls reader to populate dictionary
    parser = CSVReader.CSVReader("steam.csv")
    parser.read_file()

    adj_list: Dict[str, list] = {}

    # constructor
    def __init__(self, _dict={}, _count=0, fro='', to=''):
        self.dict = _dict
        self.count = _count
        self.fro = fro
        self.to = to

    def create_graph(self):
        #  iterate through each game in the unordered_map
        for key in self.parser.unordered_map.keys():
            this_game = self.parser.unordered_map[key]  # dictionary value isn't immediately translated to Game() object

            relevant_games: Dict[str, float] = {}
            # loop through the steamspy_tags of the game and create a dictionary (relevant_games) that has the union
            # of all the steamspy tags
            for tag in this_game.steamspy_tags:
                for curr_title in self.parser.tags_map[tag]:
                    weight = 1

                    if curr_title not in relevant_games and curr_title != this_game.name:
                        relevant_games[curr_title] = weight

                    elif curr_title in relevant_games:
                        relevant_games[curr_title] = relevant_games[curr_title] + 1

            adj_vertices = []
            for game_key in relevant_games.keys():

                relevant_games[game_key] = self.calculate_weight(this_game, game_key, relevant_games[game_key])
                relevant_games[game_key] = 1 / relevant_games[game_key]

                curr_tuple = (relevant_games[game_key], game_key)
                adj_vertices.append(curr_tuple)
                adj_vertices.sort()
                if len(adj_vertices) > 5:
                    adj_vertices.pop()

                # print(adj_vertices)

            self.adj_list[key] = adj_vertices

        # loop through the union set and at each game, calculate the similarity score and push it into a heapq (
        # minheap) of tuples (tuples being name, weight) if the heapq (minheap) has more than k elements, delete the
        # largest element push the finished heapq into a dicitonary of heapqs with the game title as key
        # reccomendations[title] = heapq

    def calculate_weight(self, this_game, curr_title: str, weight):
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
        game_numgenres = len(this_game.genres)
        # print(f'{this_game.name} has {game_numgenres} genre(s)')
        comparison_numgenres = len(comparison.genres)
        # print(f'{comparison.name} has {comparison_numgenres} genre(s)')

        if game_numgenres > comparison_numgenres:
            for genre in this_game.genres:
                if genre in comparison.genres:
                    weight += 1
                else:
                    weight -= 1

        else:
            for genre in comparison.genres:
                if genre in this_game.genres:
                    weight += 1
                else:
                    weight -= 1

        #  compare English support
        if this_game.english == comparison.english:
            weight += 1

        if this_game.english != comparison.english:
            weight -= 1

        #  compare platforms
        game_numplatforms = len(this_game.platforms)
        comparison_numplatforms = len(comparison.platforms)

        compatible = False

        if game_numplatforms < comparison_numplatforms:
            for platform in this_game.platforms:
                if platform in comparison.platforms:
                    compatible = True
        else:
            for platform in comparison.platforms:
                if platform in this_game.platforms:
                    compatible = True

        # if not compatible, cannot be adjacent
        if not compatible:
            weight = 1

        # check if weight <= 0
        if weight <= 0:
            weight = 1

        return weight

    def create_minigraph(self, search_term: str):
        #  iterate through each game in the unordered_map
        if search_term in self.parser.unordered_map.keys():
            this_game = self.parser.unordered_map[search_term]  # dictionary value isn't immediately translated to Game() object

            relevant_games: Dict[str, float] = {}
            # loop through the steamspy_tags of the game and create a dictionary (relevant_games) that has the union
            # of all the steamspy tags
            for tag in this_game.steamspy_tags:
                for curr_title in self.parser.tags_map[tag]:
                    weight = 1

                    if curr_title not in relevant_games and curr_title != this_game.name:
                        relevant_games[curr_title] = weight

                    elif curr_title in relevant_games:
                        relevant_games[curr_title] = relevant_games[curr_title] + 1

            adj_vertices = []
            for game_key in relevant_games.keys():

                relevant_games[game_key] = self.calculate_weight(this_game, game_key, relevant_games[game_key])
                relevant_games[game_key] = 1 / relevant_games[game_key]

                curr_tuple = (relevant_games[game_key], game_key)
                adj_vertices.append(curr_tuple)
                adj_vertices.sort()
                if len(adj_vertices) > 5:
                    adj_vertices.pop()

                # print(adj_vertices)

            self.adj_list[search_term] = adj_vertices

        # loop through the union set and at each game, calculate the similarity score and push it into a heapq (
        # minheap) of tuples (tuples being name, weight) if the heapq (minheap) has more than k elements, delete the
        # largest element push the finished heapq into a dicitonary of heapqs with the game title as key
        # reccomendations[title] = heapq