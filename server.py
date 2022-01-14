import os
from flask import Flask, render_template, request, jsonify, make_response
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


# Define
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(ROOT_DIR, 'upload')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Config upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/ocr', methods=['POST'])
def api_ocr():
    if 'file' not in request.files:
        return make_response(jsonify({
            "error": True,
            "msg": "file is empty"
        }), 401)
    else:
        file = request.files['file']


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    if flask_env == 'dev':
        app.run(port=port)
    else:
        serve(app=app, port=port)
