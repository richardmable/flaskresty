from flask import Flask, request
from flask_restful import Resource, Api
from flaskresty import api, app

products = {}

class HelloWorld(Resource):
    def get(self):
        return {'ola': 'amigos'}

class Product(Resource):
    def get(self, product_id):
        return {product_id: products[product_id]}

    def put(self, product_id):
        products[product_id] = request.form['data']
        return {product_id: products[product_id]}



api.add_resource(HelloWorld, '/')
api.add_resource(Product, '/products/<int:product_id>')
