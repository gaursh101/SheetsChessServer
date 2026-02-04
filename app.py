from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    with open("chess.html", "r") as file:
        content = file.read()
    return content