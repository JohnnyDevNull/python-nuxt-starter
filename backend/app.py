from flask import Flask
from flask_restful import Resource, Api
from rest_server import restApi
from socket_server import socketApi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

restApi.init_app(app)
socketApi.init_app(app)


if __name__ == '__main__':
    socketApi.run(app, host="127.0.0.1", port="5000", debug='true')
