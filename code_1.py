pip install Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])

def hello_world():
define home():
    return "Welcome to the Vivek's Flask app!"


if __name__ == '__main__':
    app.run()