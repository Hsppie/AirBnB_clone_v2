#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters')
def hbnb_filters():
     states = storage.all("State")
     amenities = storage.all("Amenity")
     return render_template("10-hbnb_filters.html", states=states, amenities=amenities)
@app.teardown_appcontext
def teardown(exc):
     storage.close

if __name__=="__main__":
     app.url_map.strict_slashes = False
     app.run(host="0.0.0.0", port=5000)
