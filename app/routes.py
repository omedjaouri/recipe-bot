from app import app

#Set up basic home routing
@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"
