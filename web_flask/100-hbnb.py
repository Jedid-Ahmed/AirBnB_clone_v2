#!/usr/bin/python3
# displays extra AirBnB location info
from flask import Flask, render_template
from models import storage
from models.state import State
from models. amenity import Amenity
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/hbnb')
def hbnb():
    # website that displays more content
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template('100-hbnb.html', **locals())


@app.teardown_appcontext
def teardown(self):
    # tears down app context
    storage.close()

if __name__ == '__main__':
    app.run(host=ip, port=port)
