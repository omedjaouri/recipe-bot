from flask import Blueprint, jsonify, request, current_app
from .util import *

#Set up blueprint
bp = Blueprint('routes', __name__, url_prefix='/')

#Set up home routing
@bp.route("/", methods=["GET"])
def home():
    return "This is a simple web-page for Recipe-Bot!"

@bp.route("/recipe", methods=["POST"])
def recipe():
    #Grab the bot to interact with
    bot = app.config['Bot']

    #Verify we received the request from Slack
    if request.form['token'] == app.config["SLACK_VERIFICATION_TOKEN"]:
        #Pass the request to RecipeBot
        text = request.form['text'].split(" ")[0]
        
        
        
        #ret = process_request(text) 
        #If user supplied bad url, return response
        #if ret is None:
        #    payload = {'text': "Sorry, but you didn't supply a valid url."}
        #    return jsonify(payload)
        #Continue to parse URL
        
        bot_string = bot.say_hello()
        payload = {'text': bot_string}
        return jsonify(payload)
