from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Let's see how fast this is"