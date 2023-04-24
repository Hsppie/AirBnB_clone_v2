#!/usr/bin/python3
"""
This script start a flask web app
listens on 0.0.0.0:5000
routes 
/  
/hbnb 
/c/<text> 
/python/(<text>) 
/number/<n> with strict_slashes=False

"""
from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def HelloHBNB():
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    return 'C' + text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>',  strict_slashes=False)
def python(text = ' is cool'):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n= None):
    
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000)