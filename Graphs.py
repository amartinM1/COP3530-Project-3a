import CSVReader
import Game


class Adjlist:
    # calls reader to populate dictionary
    global parser
    global graph
    global vert
    parser = CSVReader.CSVReader("steam.csv")
    parser.read_file()
    obj = Game.Game()

    # constructor
    def __init__(self, _dict={}, _count=0, fro='', to=''):
        self.dict = _dict
        self.count = _count
        self.fro = fro
        self.to = to

    def vertex(self):

        for key in parser.unorderedMap.keys():

            if key in self.dict:
                print(key, "is already a vertex in the graph")
            else:
                self.count += 1
                self.dict[key] = list()

    def edge(self):

        for key in self.dict.keys():
            weight = 0
            temp = parser.unorderedMap[key]
            for tag in temp.steamspy_tags:
                for x in temp.tags_map[tag]:

                    if x not in self.dict[key]:
                        temp_tuple = (x, weight)
                        self.dict[key].append[temp_tuple]
                    if x in self.dict[key]:
                        weight = weight + 1
                        temp_tuple = (x, weight)
                        self.dict[key].append[temp_tuple]
