from flask import Flask
from waitress import serve


class Server:

    _flask: Flask = Flask(__name__)

    # Initial server flask
    # Run app on 8080
    @staticmethod
    def initialization():
        serve(Server._flask, port=8080)

    @staticmethod
    def instance() -> Flask:
        return Server._flask
