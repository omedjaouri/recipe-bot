from flask import Flask
from config import Config

def create_app(bot_instance):
    #Create flask app and pass bot instance
    app = Flask(__name__)

    #Get config variables from the environment
    app.config.from_object(Config)
    
    #Pass instance of bot
    app.config['Bot'] = bot_instance

    #Import blueprints
    from . import routes
    app.register_blueprint(routes.bp)

    return app

