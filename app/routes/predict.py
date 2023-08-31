import numpy as np
from app.models.input_schema import schema
import joblib
from flask import request, jsonify
from app.utils.preprocessing import mens_to_input
from app.utils.siri import compute_siri
from cerberus import Validator
from app import app
from flask_cors import cross_origin
from flask_cors import CORS


cors = CORS(app)
model = joblib.load("app/services/rf_bodyfat_estimator.pkl")
scaler = joblib.load("app/services/scaler_bodyfat_estimator.pkl")

input_schema = schema
validator = Validator(input_schema)


@app.route("/test")
def test():
    return jsonify({"prediction": "GOOD !"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        if not validator.validate(data):
            raise AssertionError("Please give a valid input.")

        input = mens_to_input(data)

        input_scaled = scaler.transform(input)

        prediction = model.predict(input_scaled)

        bodyfat = np.round(compute_siri(prediction[0]), 2)

        return jsonify({"prediction": bodyfat}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run()
