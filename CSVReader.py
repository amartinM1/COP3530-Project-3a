import csv
import Game
from typing import Dict


class CSVReader:
    unordered_map: Dict[str, Game.Game] = {}  # Game objects stored by title
    tags_map = {}  # Game titles stored by steamspy_tags

    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(self.file, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:  # each row is (value [delim] value [delim] etc...)
                row["categories"] = row["categories"].split(';')
                row["developer"] = row["developer"].split(';')
                row["genres"] = row["genres"].split(';')
                row["steamspy_tags"] = row["steamspy_tags"].split(';')
                row["platforms"] = row["platforms"].split(';')
                if '®' in row["name"] or '™' in row["name"]:
                    row["name"] = row["name"].replace('®', '')
                    row["name"] = row["name"].replace('™', '')
                game = Game.Game(row["name"], row["developer"], row["categories"], row["genres"], row["steamspy_tags"],
                                 row["english"], row["platforms"])
                self.unordered_map[game.name] = game
                for key in game.steamspy_tags:
                    if key not in self.tags_map:
                        self.tags_map[key] = list()
                    self.tags_map[key].append(game.name) # what is this

    def get_unordmap(self):
        return self.unordered_map
