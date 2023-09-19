#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

@app.route("/")
def index():
    return "My Flask App"

if __name__== '__main__':
 app.run(port=555)