"""The socketio package."""

from flask_socketio import SocketIO, emit
from socket_server.handler.client_connect import client_connect
from socket_server.handler.client_disconnect import client_disconnect

socketApi = SocketIO()
socketApi.on('connect', client_connect)
socketApi.on('disconnect', client_disconnect)
