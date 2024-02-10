import time
import socketio
from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from random import randint

PLAYERS_PER_GAME = 4
activeGames = []

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

    def add_player(self, player):
        if len(self.players) < PLAYERS_PER_GAME:
            self.players.append(player)
            print(f"Player {player} joined the game.")
        else:
            print("Maximum players reached for this game.")

    def start_game(self):
        if len(self.players) == PLAYERS_PER_GAME:
            print("Starting the game...")
            # Implement logic to start the game here
            pass
        else:
            print("Not enough players to start the game.")

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
    game = Game(gameID, language, numPlayers)
    activeGames.append(game)

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
def join(data):
    print(data)
    gameID = data['gameID']
    username = data['username']
    sid = request.sid  # Get the session ID of the client

    # Find the game
    game = next((game for game in activeGames if game.id == gameID), None)
    if game is None:
        socketio.emit('gameNotFound')
        return

    player = Player(username, sid)
    game.add_player(player)

    if len(game.players) == PLAYERS_PER_GAME:
        socketio.emit('startGame')  # Notify everyone
    else:
        socketio.emit('updatePlayers', [str(player) for player in game.players])  # Update player list

if __name__ == '__main__':
    socketio.run(app, debug=True)
