from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return ("Hello World welcome to Vivek's Flask Application!")

@app.route('/get_square', methods=['POST'])
def get_square():
    data = request.get_json()
    number = data.get('number')
    return jsonify({'number': number**2})

if __name__ == '__main__':
    app.run()