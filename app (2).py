
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model pipeline
# Make sure model.pkl is in the same directory as app.py or a path accessible by Vercel
model_pipeline = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Telco Churn Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_data = request.get_json(force=True)
        # Convert input data to a DataFrame
        # Ensure the column order matches the training data
        df_input = pd.DataFrame([json_data])
        
        # Make prediction
        prediction = model_pipeline.predict(df_input)
        prediction_proba = model_pipeline.predict_proba(df_input)[:, 1]

        churn_status = "Yes" if prediction[0] == 1 else "No"
        
        return jsonify({
            'churn_prediction': churn_status,
            'churn_probability': float(prediction_proba[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
