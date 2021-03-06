from app import app
from flask import jsonify, request
from .util import *

#Set up home routing
@app.route("/", methods=["GET"])
def home():
    return "This is a simple web-page for Recipe-Bot!"

@app.route("/recipe", methods=["POST"])
def recipe():
    #Verify we received the request from Slack
    if request.form['token'] == app.config["SLACK_VERIFICATION_TOKEN"]:
        #Pass the request to RecipeBot
        text = request.form['text'].split(" ")[0]
        ret = process_request(text) 
        #If user supplied bad url, return response
        if ret is None:
            payload = {'text': "Sorry, but you didn't supply a valid url."}
            return jsonify(payload)
        #Else, return the recipe the user requested
        payload = {'text': ret}
        return jsonify(payload)
