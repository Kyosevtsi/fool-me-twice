from flask import Flask, jsonify, request
import pymongo
import threading
import Game
from random import randint
from flask_socketio import SocketIO

activeGames = []

# Initialize the app
app = Flask(__name__)
socketio = SocketIO(app)
app.config['MONGODB_SETTINGS'] = { 'db': 'placeholder' }

# ... Other API routes ...
@app.route('/api/placeholder', methods=['GET'])
def get_placeholder():
    return jsonify({ 'message': 'Placeholder' })

@app.route('/createLobby', methods=['POST'])
def createLobby():
    # get url params 
    data = request.args
    language = data['language']
    numPlayers = data['numPlayers']

    # create a new game
    gameID = randint(1000, 9999)
    game = Game.Game(gameID, language, numPlayers)
    activeGames.append(game)   

    return jsonify({ 'gameID': gameID })

# websocket 
@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

@socketio.on('join')
def join(data):
    print(data)
    gameID = data['gameID']
    username = data['username'] 

    # find the game
    game = next((game for game in activeGames if game.id == gameID), None)
    if game is None:
        emit('gameNotFound', broadcast=True)
        return
    
    game.players.append({'sid': sid, 'username': username, score: 0})

    if len(players) == PLAYERS_PER_GAME:
        emit('startGame', broadcast=True)  # Notify everyone
    else:
        emit('updatePlayers', players, broadcast=True)  # Update player list


if __name__ == '__main__':
    app.run(debug=True)

