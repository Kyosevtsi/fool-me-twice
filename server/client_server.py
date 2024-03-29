import time
import socketio
from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS
from random import randint, choice
import threading
import json

TIME_PER_QUESTION = 32
NUMBER_OF_ROUNDS = 5
activeGames = set()

class Player:
    def __init__(self, name, sid, pid):
        self.name = name
        self.score = 0
        self.sid = sid
        self.id = pid

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
        print("Game with ID " + str(self.id) + " has started.")
        # send the start events to the client
        socketio.emit('gameStarting', {'gameID': self.id})
        time.sleep(3)
        socketio.emit('gameStarted', {'gameID': self.id})

        # load the translations
        f = open('../translations.json', 'r')
        translations = json.load(f)
        round = 0

        used_indeces = set()
        while round < NUMBER_OF_ROUNDS:
            round += 1
            print(f"Round {round}!")
            # translations['translations'] is the list of translations
            rand_index = randint(0, len(translations['translations']) - 1)
            while rand_index in used_indeces:
                rand_index = randint(0, len(translations['translations']) - 1)
            questionObj = translations['translations'][rand_index]
            used_indeces.add(rand_index)

            question = questionObj['Other'][int(self.language)]
            socketio.emit('question', {'gameID': self.id, 'payload': question})

            # Start the timer
            start_time = time.time()

            # Reset response flag for each player
            responses_received = {player.sid: False for player in self.players}

            # Wait for responses or timeout
            while (time.time() - start_time) < TIME_PER_QUESTION:
                all_responded = all(responses_received.values())
                if all_responded:
                    break
                time.sleep(0.1)

            # get the responce
                
            # chop it down to feed into the AI
                
            # create a potential answer pool ---> display the pool
            
            # 15 seconds to pick the right answer
                
            # process the input and dispay the selections
                
            # calculate the points
                
            # end of the round
                

        f.close()
        pass

    def add_player(self, player):
        if len(self.players) < self.numPlayers:
            self.players.append(player)
            #socketio.emit('playerJoined', {'player': str(player),'playerID': player.pid ,'gameID': self.id})
            #player_info = [{'name': p.name, 'id': p.id} for p in self.players]
            #socketio.emit('updatePlayers', {'gameID': self.id, 'players': player_info})
            socketio.emit('updatePlayers', [str(player) for player in self.players])
            print(f"Player {player} joined the game.")

# Initialize the Flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# API routes
@app.route('/api/placeholder', methods=['GET'])
def get_placeholder():
    return jsonify({'message': 'Placeholder'})

@app.route('/createLobby', methods=['GET'])
def createLobby():
    data = request.args
    language = data['language']
    numPlayers = int(data['numPlayers'])
    hostName = data['name']

    # Create a new game
    gameID = randint(1000, 9999)
    if len(activeGames) > 0: 
        while gameID in activeGames:
            gameID = randint(1000, 9999)
    game = Game(gameID, language, numPlayers)
    activeGames.add(game)

    # Create a new player
    player = Player(hostName, request.sid, 1)
    game.add_player(player)

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

    new_player_pid = len(game.players) + 1
    player = Player(username, 0, sid, new_player_pid)
    game.add_player(player)
    # socketio.emit('updatePlayers', [str(player) for player in game.players])  # Update player list

    if len(game.players) == game.numPlayers:
        socketio.emit('startGame')  # Notify everyone
        game.gameState = 'playing'

@socketio.on('response')
def response(rawData):
    data = json.loads(rawData)
    gameID = data['gameID']
    response = data['response']
    sid = request.sid

    game = next((game for game in activeGames if game.id == gameID), None)
    if game is None:
        socketio.emit('gameNotFound')
        return

    player = next((player for player in game.players if player.sid == sid), None)
    if player is None:
        socketio.emit('playerNotFound')
        return

    game.responses.append({
        'player': player,
        'response': response
    })

if __name__ == '__main__':
    socketio.run(app, debug=True)
