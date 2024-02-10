import time
import socketio

PLAYERS_PER_GAME = 4
class Game:
    def __init__(self, gameID, language, numPlayers):
        self.id = gameID
        self.language = language
        self.numPlayers = numPlayers
        self.players = []
        self.gameState = 'waiting'
        self.round = 0
        self.gameLoop()

    def gameLoop(self):
        # generate the web socket server
        sio = socketio.Server()
        app = socketio.WSGIApp(sio)
        print("The game has started. Game ID: " + str(self.id))

        @sio.event
        def disconnect(sid):
            print('disconnect ', sid)

        @sio.event
        def connect(sid, data): 
            print('connect ', sid)
            username = data['username']  # Assuming username is sent from client

            player = Player.Player(username)
            players.append(player)

            if len(players) == PLAYERS_PER_GAME:
                emit('startGame', broadcast=True)  # Notify everyone
            else:
                emit('updatePlayers', players, broadcast=True)  # Update player list

    # Actual game logic has to be implemented here (e.g send questions to clients, recieve answers from clients, send timeout requests, etc.)

    