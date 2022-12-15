from flask import Flask, render_template
from flask_socketio import SocketIO

import redis

# Connect to the Redis server
r = redis.Redis()

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def on_connect( ):

    print('A new client has connected!')
    
    # Save the player's data using the set() method
    #r.set("player1", "John Doe")


@socketio.on('disconnect')
def on_disconnect():
    print('A client has disconnected!')

# Listen for the 'button-clicked' event
@socketio.on("button-clicked")
def handle_button_click(message):
    print("\n\nYO PLAYER BUTTON CLICKED\n\n")
  
@app.route('/')
def index():
    return render_template('game.html')

if __name__ == '__main__':
    socketio.run(app)