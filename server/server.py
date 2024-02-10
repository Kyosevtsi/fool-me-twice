from flask import Flask, jsonify, request
import pymongo
import threading
import Game
from random import randint

# Initialize the app
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = { 'db': 'placeholder' }

# /createLobby?language=russian&numPlayers=3

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

    gameID = randint(1000, 9999)
    game = Game.Game(gameID, language, numPlayers)

    # create the game event loop
    threading.Thread(target=game.gameLoop).start()

    return jsonify({ 'gameID': gameID })

if __name__ == '__main__':
    app.run(debug=True)