# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome1():
    return "welcome to may first flask app"

if __name__ == "__main__":
    app.run()
