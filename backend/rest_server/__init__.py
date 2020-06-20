"""The REST api package."""

from flask_restful import Api
from rest_server.controller.index import IndexController

rest_api = Api()
rest_api.add_resource(IndexController, '/')
