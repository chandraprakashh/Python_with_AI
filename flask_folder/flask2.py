# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 22:28:38 2019

@author: BSDU ADMIN
"""

import flask

from flask import Flask
app = Flask(__name__)

@app.route("/SKP1")
def welcome3():
    return "welcome to may first flask app"


app.run(host='0.0.0.0', port= 81)
if __name__ == "__main__":
    app.run()

