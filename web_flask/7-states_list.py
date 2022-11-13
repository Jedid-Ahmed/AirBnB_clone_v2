#!/usr/bin/python3
# displays states
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/states_list')
def states_list():
    # lists the states
    all_states = list(storage.all(State).values())
    return (render_template('7-states_list.html', all_states=all_states))


@app.teardown_appcontext
def teardown(self):
    # tears down app context
    storage.close()

if __name__ == "__main__":
    app.run(host=ip, port=port)
