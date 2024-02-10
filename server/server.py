from flask import Flask, jsonify, request
import pymongo
import threading
import game

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

    # create the game event loop
    threading.Thread(target=Game, args=(language, numPlayers)).start()


    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)