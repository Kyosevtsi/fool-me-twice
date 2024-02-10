class Player:
    def __init__(self, name, pID):
        self.name = name
        self.id = pID
        self.score = 0

    def __str__(self):
        return self.name