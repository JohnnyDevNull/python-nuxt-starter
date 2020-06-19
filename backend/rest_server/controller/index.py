from flask_restful import Resource

class IndexController(Resource):
    def get(self):
        return {'message': 'The API is online!'}
