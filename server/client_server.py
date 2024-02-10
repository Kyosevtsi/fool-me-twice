import time
import socketio
from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from random import randint, choice
import threading
import json

PLAYERS_PER_GAME = 4
activeGames = set()

class Player:
    def __init__(self, name, sid):
        self.name = name
        self.score = 0
        self.sid = sid

    def __str__(self):
        return self.name

class Game:
    def __init__(self, gameID, language, numPlayers):
        self.id = gameID
        self.language = language
        self.numPlayers = numPlayers
        self.players = []
        self.gameState = 'waiting'
        self.round = 0

    def event_loop(self):
        print("The game has started. Game ID: " + str(self.id))
        
        while self.gameState == 'waiting':
            time.sleep(1)

        # Implement game logic here
        # send the questions to the clients
        # recieve the answers from the clients
        # send timeout requests (when time expries)

        print("Game with ID " + str(self.id) + " has started.")
        # send the start events to the client
        socketio.emit('gameStarting', {'gameID': self.id})
        time.sleep(3)
        socketio.emit('gameStarted', {'gameID': self.id})

        # load the translations
        f = open('../translations.json', 'r')
        translations = json.load(f)

        used_indeces = set()
        while True:
            # translations['translations']
            rand_index = randint(0,(len(translations['translations'])-1))
            print(rand_index)
            while rand_index in used_indeces:
                rand_index = randint(0,(len(translations['translations'])-1))
            questionObj = translations['translations'][rand_index]
            used_indeces.add(rand_index)
            # questionObj = choice(translations['translations'])
            question = questionObj['Other'][int(self.language)]
            socketio.emit('question', {'gameID': self.id, 'payload': question})

        f.close()
        pass

    def add_player(self, player):
        if len(self.players) < PLAYERS_PER_GAME:
            self.players.append(player)

            socketio.emit('playerJoined', {'player': str(player), 'gameID': self.id})
            print(f"Player {player} joined the game.")

    # def start_game(self):
    #     if len(self.players) == PLAYERS_PER_GAME:
    #         print("Starting the game...")
    #         # Implement logic to start the game here
    #         pass
    #     else:
    #         print("Not enough players to start the game.")

# Initialize the Flask app
app = Flask(__name__)
socketio = SocketIO(app)

# API routes
@app.route('/api/placeholder', methods=['GET'])
def get_placeholder():
    return jsonify({'message': 'Placeholder'})

@app.route('/createLobby', methods=['POST'])
def createLobby():
    data = request.args
    language = data['language']
    numPlayers = int(data['numPlayers'])

    # Create a new game
    gameID = randint(1000, 9999)
    if len(activeGames) > 0: 
        while gameID in activeGames:
            gameID = randint(1000, 9999)
    game = Game(gameID, language, numPlayers)
    activeGames.add(game)

    threading.Thread(target=game.event_loop).start()

    return jsonify({'gameID': gameID})

# WebSocket events
@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')
    sid = request.sid
    # Remove the disconnected player from active games
    for game in activeGames:
        game.players = [player for player in game.players if player.sid != sid]

@socketio.on('join')
def join(rawData):
    data = json.loads(rawData)
    gameID = data['gameID']
    username = data['username']
    sid = request.sid  # Get the session ID of the client

    # Find the game
    game = next((game for game in activeGames if game.id == gameID), None)
    if game is None:
        socketio.emit('gameNotFound')
        return

    if (game.gameState != 'waiting'):
        socketio.emit('gameInProgress')
        return

    player = Player(username, sid)
    game.add_player(player)

    if len(game.players) == PLAYERS_PER_GAME:
        socketio.emit('startGame')  # Notify everyone
        game.gameState = 'playing'
    else:
        socketio.emit('updatePlayers', [str(player) for player in game.players])  # Update player list

if __name__ == '__main__':
    socketio.run(app, debug=True)
