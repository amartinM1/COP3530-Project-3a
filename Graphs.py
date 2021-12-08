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
                self.dict[key] = [tuple()]

    def edge(self):

        for key in self.dict.keys():
            weight = 0
            temp = parser.unorderedMap[key]
            for tag in temp.steamspy_tags:
                for x in parser.tags_map[tag]:
                    # create a variable that represents  a list of the first variables in the tuple
                    # [item for item in a if item[0] == 1]
                    temp_list = self.dict[key]
                    for i in temp_list:
                        if x not in i[0]:
                            temp_tuple = (x, weight)
                            # gamename=temp_tuple[0]
                            temp_list.append[temp_tuple]
                        if x in i[0]:
                            weight = weight + 1
                            # temp_tuple = (x, weight)
                            i[1] = weight

    def createGraph(self):
        #  iterate through each game in the unordered_map
        #  loop through the steamspy_tags of the game and create a set that has the union of all the steamspy tags
        #  loop through the union set and at each game, calculate the similarity score and push it into a heapq (minheap)
        #  if the heapq (minheap) has more than k elements, delete the largest element
        #  push the finished heapq into a dicitonary of heapqs with the game title as key reccomendations[title] =heapq

