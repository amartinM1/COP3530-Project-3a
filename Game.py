class Game:

    def __init__(self, _name="", _developer="", _categories="", _genres="", _steamspy_tags=""):
        self.name = _name
        self.developer = _developer
        self.categories = _categories  # Vector
        self.genres = _genres  # Vector
        self.steamspy_tags = _steamspy_tags

    def print(self):
        print(self.name)
        print(self.developer)
        print(self.genres)
        print(self.steamspy_tags)
        print(self.categories)
