from flask import Flask, render_template, url_for
from waitress import serve


class Server:

    _flask: Flask = Flask(
        __name__, template_folder="../resources/views", static_folder="../resources")

    # Initial server flask
    # Run app on 8080

    @staticmethod
    def initialization():
        serve(Server._flask, port=8080)
