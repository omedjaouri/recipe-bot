from app import app
from flask import jsonify, request

#Set up home routing
@app.route("/", methods=["GET"])
def home():
    return "This is a simple web-page for Recipe-Bot!"

@app.route("/hello", methods=["POST"])
def hello():
    return "Hello Slack!"

@app.route("/recipe", methods=["POST"])
def recipe():
    print(request)
    #Verify we received the request from Slack
    if request.form['token'] == app.config["SLACK_VERIFICATION_TOKEN"]:
        payload = {'text': 'Thanks for sending a recipe to me!'}
        return jsonify(payload)
