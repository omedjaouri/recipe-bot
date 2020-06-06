import os
from flask import Flask, request, make_response, render_template

#Set up App
app = Flask(__name__)

#Set up home routing
@app.route("/", methods=["GET"])
def home():
    return "Hello World!"

@app.route("/hello", methods=["POST"])
def hello():
    return "Hello Slack!"

#Run the app
if __name__ == "__main__":
    app.run()
