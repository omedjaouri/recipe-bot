from flask import Flask
from config import Config

def create_app(bot_instance):
    #Create flask app and pass bot instance
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['Bot'] = bot_instance
    return app

from app import routes
