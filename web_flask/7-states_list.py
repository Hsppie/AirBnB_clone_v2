#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)



@app.route('/states_list')
def state_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states = states)

@app.teardown_appcontext
def teardown(exc):
    storage.close()





if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port= 5000)
