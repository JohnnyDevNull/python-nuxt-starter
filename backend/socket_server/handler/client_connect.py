from flask_socketio import emit


def client_connect():
    emit('init', {'message': 'The socket is online'})
