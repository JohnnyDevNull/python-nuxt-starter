"""The socketio package."""

from flask_socketio import SocketIO, emit
from socket_server.handler.client_connect import client_connect
from socket_server.handler.client_disconnect import client_disconnect

socket_api = SocketIO()
socket_api.on('connect', client_connect)
socket_api.on('disconnect', client_disconnect)
