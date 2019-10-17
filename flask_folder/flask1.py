# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:26:24 2019

@author: BSDU ADMIN
"""

import flask

from flask import Flask
app = Flask(__name__)

@app.route("/SKP")
def welcome1():
    return "welcome to may first flask app"

if __name__ == "__main__":
    app.run()
