#!/usr/bin/python3
# web app that connects our html from previous project
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/hbnb_filters')
def hbnb():
    # website that connects html and css
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    # tears down app context
    storage.close()

if __name__ == '__main__':
    app.run(host=ip, port=port)
