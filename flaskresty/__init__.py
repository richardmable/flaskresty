from flask import Flask
# from flask_sslify import SSLify
from werkzeug.debug import DebuggedApplication
from flask_restful import Resource, Api

app = Flask(__name__)
# force https
# sslify = SSLify(app)
api = Api(app)
# don't do this in production
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

import flaskresty.views