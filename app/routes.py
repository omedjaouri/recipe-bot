from app import app
from flask import jsonify, request

#Set up home routing
@app.route("/", methods=["GET"])
def home():
    return "This is a simple web-page for Recipe-Bot!"

@app.route("/recipe", methods=["POST"])
def recipe():
    #Verify we received the request from Slack
    if request.form['token'] == app.config["SLACK_VERIFICATION_TOKEN"]:
        #Pass the request to RecipeBot
        print(request.form.keys())
        print(request.form['text']) 
        payload = {'text': 'Thanks for sending a recipe to me!'}
        return jsonify(payload)
