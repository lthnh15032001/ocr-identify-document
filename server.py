from flask import Flask, render_template
from waitress import serve

app: Flask = Flask(__name__)


@app.route('/')
def splash():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    serve(app=app, port=8080)
