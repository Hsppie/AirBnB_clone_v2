#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/states")
def state():
    states = storage.all("State")
    return render_template("9-states.html", states=states)

@app.route("/states/<int:id>")
def state_by_id(id):
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state= state)
    return render_template("9-states.html")

if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
