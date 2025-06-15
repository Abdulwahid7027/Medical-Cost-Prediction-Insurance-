from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib
from utils.preprocess import preprocess_input

app = Flask(__name__)
CORS(app)

xgb_model = joblib.load('models/xgb_model.pkl')
lgbm_model = joblib.load('models/lgbm_model.pkl')
catboost_model = joblib.load('models/catboost_model.pkl')

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to Medical Cost Prediction API'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = preprocess_input(data)
        xgb_pred = xgb_model.predict(input_data)
        lgbm_pred = lgbm_model.predict(input_data)
        catboost_pred = catboost_model.predict(input_data)
        hybrid_pred = (xgb_pred + lgbm_pred + catboost_pred) / 3
        prediction = np.expm1(hybrid_pred)[0]
        return jsonify({
            'status': 'success',
            'prediction': round(prediction, 2)
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)