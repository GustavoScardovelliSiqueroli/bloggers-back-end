from flask import Flask
from bloggers.ext import configuration

def minimal_app(**config):
    app = Flask(__name__, instance_relative_config=True)
    configuration.init_app(app, **config)
    return app

def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app