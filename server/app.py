#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Sup Gente!</h1>"

@app.route("/<string:username>")
def show(username):
    return f"<h1>Sup {username}!</h1>"


# from command line
if __name__ == '__main__':
    app.run(port=5555, debug=True)