from flask import Flask
from flask_restful import Resource, Api
from flaskresty import api, app

class HelloWorld(Resource):
    def get(self):
        return {'ola': 'amigos'}

api.add_resource(HelloWorld, '/')
