import time
import socketio

class Game:
    def __init__(self, gameID, language, numPlayers):
        self.id = gameID
        self.language = language
        self.numPlayers = numPlayers
        self.players = []
        self.gameState = 'waiting'
        self.gameLoop()

    def gameLoop(self):
        # create the socket
        sio = socketio.Server()
        app = socketio.WSGIApp(sio)

        # Create the game event loop
        @sio.event
        def connect(sid, environ):
            print(f'Client connected: {sid}')
            if len(self.players) < self.numPlayers:
                self.addPlayer(sid)
                if len(self.players) == self.numPlayers:
                    self.gameState = 'active'
                    sio.emit('game_start')  # Notify players game has begun
            else:
                sio.emit('game_full', to=sid)

        @sio.event
        def disconnect(sid):
            print(f'Client disconnected: {sid}')
            self.players.remove(sid)  
            if self.gameState == 'active':
                # Handle player leaving mid-game (e.g., notify others)
                pass  

        # ... Add more event handlers as needed: 
        #     @sio.event
        #     def game_action(sid, data):
        #         # Handle game actions and logic

        # Start the server (replace with appropriate hosting if needed)
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app) 

        # create the game event loop
    
    def addPlayer(self, player):
        self.players.append(player)
        print(self.players)