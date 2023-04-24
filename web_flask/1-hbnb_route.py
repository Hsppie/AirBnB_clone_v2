#!/usr/bin/python3
"""
This script start a flask web app
listens on 0.0.0.0:5000
routes / , /hbnb with strict_slashes=False

"""
from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def HelloHBNB():
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port= 5000)
