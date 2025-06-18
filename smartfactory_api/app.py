from flask import Flask, request, jsonify
from predict import faire_prediction

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def prediction():
    data = request.get_json()
    try:
        resultat = faire_prediction(data)
        return jsonify({"prediction": int(resultat)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
