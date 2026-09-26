from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sai-chat-secret'
socketio = SocketIO(app, cors_allowed_origins="*")
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    users[data['sid']] = data['username']
    emit('user_joined', {'username': data['username']}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    emit('new_message', {'username': data['username'], 'message': data['message']}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    users.pop(str(id), None)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    socketio.run(app, host='0.0.0.0', port=port)
