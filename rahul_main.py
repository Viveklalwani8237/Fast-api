from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
with open("iris_classifier_rahul.pkl","rb") as fileobj:
    iris_model = pickle.load(fileobj)

@app.route('/', methods=['GET'])
def home():
    return "Hello World welcome to Rahul's Flask Application!"

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    SepalLengthCm = data.get("sl")
    SepalWidthCm = data.get("sw")
    PetalLengthCm = data.get("pl")
    PetalWidthCm = data.get("pw")
    flower_type = iris_model.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])
    return jsonify({"predicted_flower_type": flower_type[0]})

if __name__ == '__main__':
    app.run()
