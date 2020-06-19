"""The REST api package."""

from flask_restful import Api
from rest_server.controller.index import IndexController

restApi = Api()
restApi.add_resource(IndexController, '/')
