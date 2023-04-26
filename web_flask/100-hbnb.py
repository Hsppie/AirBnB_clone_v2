#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.place import Place
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)

@app.route("/hbnb")
def hbnb():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html", states=states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown(exc):
    storage.close()

if __name__=="__main___":
    app.url_map.strict_slashes =False
    app.run(host="0.0.0.0", port=5000)
