class Game:
    def __init__(self, language, numPlayers):
        self.language = language
        self.numPlayers = numPlayers
        self.players = []
        self.gameState = 'waiting'
        self.gameLoop()

    def gameLoop(self):
        while True:
            if self.gameState == 'waiting':
                if len(self.players) == self.numPlayers:
                    self.gameState = 'playing'
            elif self.gameState == 'playing':
                self.gameState = 'waiting'
                self.players = []
            else:
                print('Invalid game state')
                break
            time.sleep(1)
    
    def addPlayer(self, player):
        self.players.append(player)
        print(self.players)