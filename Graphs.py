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
                self.dict[key] = []

    def edge(self):

       for key in self.dict.keys():
            for values in parser.unorderedMap.values():
                for i in range(len(values.categories)):
                     if parser.unorderedMap[key].categories == values.categories:
                # access each individual attribute of the game
                #weight = 
                 # node = [values, weight]
              # var = self.dict[key].append[node]