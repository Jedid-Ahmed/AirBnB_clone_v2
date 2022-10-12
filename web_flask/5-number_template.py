#!/usr/bin/python3
# starts a Flask web app
from flask import Flask
from flask import render_template
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


@app.route('/c/<text>')
def c_text(text):
    # returns user text with C in front
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    # returns user text with python in front
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def num(n):
    # returns an integer
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def num_template(n):
    # return html if n is an int
    return (render_template('5-number.html', n=n))

if __name__ == "__main__":
    app.run(host=ip, port=port)
