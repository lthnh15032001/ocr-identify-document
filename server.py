from flask import Flask, render_template
from waitress import serve

app: Flask = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')


if __name__ == '__main__':
    serve(app=app, port=8080)
