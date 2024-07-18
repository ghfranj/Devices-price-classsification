import os
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, request, jsonify
from model import PricePredictionModel

app = Flask(__name__)

# Load the prediction model
model_path = os.getenv("MODEL_PATH", "saved_model/best_model.h5")
prediction_model = PricePredictionModel(model_path=model_path)

@app.route('/')
def home():
    return "Price Prediction Model API"

@app.route('/predict_single', methods=['POST'])
def predict_single():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input data to DataFrame for preprocessing
        input_data = pd.DataFrame([data])
        prediction = prediction_model.predict_single(input_data)
        probability = prediction_model.predict_proba(input_data)

        return jsonify({
            "prediction": int(prediction[0]),
            "probability": probability.tolist()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict_group', methods=['POST'])
def predict_group():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input data to DataFrame for preprocessing
        input_data = pd.DataFrame(data)
        predictions = prediction_model.predict_group(input_data)

        return jsonify({
            "predictions": predictions.tolist()
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
