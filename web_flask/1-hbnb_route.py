#!/usr/bin/python3
# starts a Flask web app
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/')
def hello_hbnb():
    # says Hello HBNB when curl'd
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    # displays HBNB
    return ("HBNB")

if __name__ == "__main__":
    app.run(host=ip, port=port)
