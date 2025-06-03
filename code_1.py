<<<<<<< HEAD
pip install Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])

def hello_world():
define home():
    return "Welcome to the Vivek's Flask app!"


if __name__ == '__main__':
=======
pip install Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])

def hello_world():
define home():
    return "Welcome to the Vivek's Flask app!"


if __name__ == '__main__':
>>>>>>> 55f5296b74f46e31122e64038cd44a94c910a1a8
    app.run()