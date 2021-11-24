from flask import Flask
from waitress import serve


class Server:

    _flask: Flask

    def __init__(self):
        self._flask = Flask(__name__)

    # Initial server flask
    # Run app on 8080
    def initialization(self):
        serve(self._flask, port=8080)
