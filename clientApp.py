from flask import Flask, request, jsonify, render_template
from ai_utils.utils import decodeImage
from predict import dogcat



app = Flask(__name__)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = dogcat(self.filename)



@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')
    


@app.route("/predict", methods=['POST'])
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8000, debug=True)
