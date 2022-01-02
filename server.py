import os
from flask import Flask, render_template
from waitress import serve
from dotenv import load_dotenv

# Load configuration environment
load_dotenv()

# Initialization application
app: Flask = Flask(__name__)

# Read variable environment port
port = os.getenv('PORT')
if port == None:
    port = 8080
else:
    port = int(port)

# Read variable environment
flask_env = os.getenv('FLASK_ENV')


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    if flask_env == 'dev':
        app.run(port=port)
    else:
        serve(app=app, port=port)
