from flask import Flask
from rest_server import rest_api
from socket_server import socket_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

rest_api.init_app(app)
socket_api.init_app(app)


if __name__ == '__main__':
    socket_api.run(app, host="127.0.0.1", port="5000", debug='true')
