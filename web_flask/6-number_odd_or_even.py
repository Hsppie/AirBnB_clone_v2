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
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def HelloHBNB():
    return 'Hello HBNB'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def C_is_fun(text):
    return 'C' + text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>')
def python(text = ' is cool'):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>')
def number(n= None):
    return str(n) + ' is a number'


@app.route('/number_template/')
@app.route('/number_template/<int:n>')
def number_template(n=None):
    nu = 'Number: ' + str(n)
    return render_template('5-number.html', nu=nu )

@app.route('/number_odd_or_even/')
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n=None):
    if n%2 == 0:
        nu = 'Number: ' + str(n) + ' is even'
        return render_template('6-number_odd_or_even.html', nu=nu )
    else:
        nu = 'Number: ' + str(n) + ' is Odd'
        return render_template('6-number_odd_or_even.html', nu=nu )



if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port= 5000)