#!/usr/bin/python3
"""
flask web app
listen on 0.0.0.0:5000, 
route / displays Hello HBNB! with strict_slashes=False
"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def HelloHBNB():
    return 'Hello HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000)

