from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import pandas as pd
from mlproject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

class DataPreprocessor:
    """Handle data preprocessing to match training data format exactly"""
    
    def __init__(self):
        # Define label encoding mappings (must match training)
        self.label_encodings = {
            'gender': {'Female': 0, 'Male': 1},
            'Partner': {'No': 0, 'Yes': 1},
            'Dependents': {'No': 0, 'Yes': 1},
            'PhoneService': {'No': 0, 'Yes': 1},
            'PaperlessBilling': {'No': 0, 'Yes': 1}
        }
        
        # Define columns that get one-hot encoded
        self.onehot_columns = [
            'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
            'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 
            'Contract', 'PaymentMethod'
        ]
    
    def preprocess_data(self, data_dict):
        """
        Convert raw form data to the format expected by the trained model
        This matches your exact training preprocessing steps
        """
        # Convert to DataFrame
        df = pd.DataFrame([data_dict])
        
        # Handle TotalCharges - convert to numeric (same as training)
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        # Note: In training you dropped NaN rows, but for prediction we'll fill with 0
        df['TotalCharges'].fillna(0, inplace=True)
        
        # Ensure SeniorCitizen is int
        df['SeniorCitizen'] = df['SeniorCitizen'].astype(int)
        
        # Apply label encoding (same as training)
        label_encode_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
        for col in label_encode_cols:
            if col in df.columns:
                df[col] = df[col].map(self.label_encodings[col])
        
        # Apply one-hot encoding (same as training)
        for col in self.onehot_columns:
            if col in df.columns:
                df = pd.get_dummies(df, columns=[col], prefix=col, drop_first=False)
        
        # Convert any boolean columns to int (same as training)
        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)
        
        return df

# Initialize preprocessor
preprocessor = DataPreprocessor()

# Home Page
@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

# Training Route
@app.route('/train', methods=['POST'])
def training():
    try:
        os.system('python main.py')   # Runs your training pipeline
        return "✅ Training completed successfully!"
    except Exception as e:
        return f"❌ Training failed: {str(e)}", 500

# Prediction Form Page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect user input from the form
            data = {
                "gender": request.form['gender'],
                "SeniorCitizen": int(request.form['SeniorCitizen']),
                "Partner": request.form['Partner'],
                "Dependents": request.form['Dependents'],
                "tenure": int(request.form['tenure']),
                "PhoneService": request.form['PhoneService'],
                "MultipleLines": request.form['MultipleLines'],
                "InternetService": request.form['InternetService'],
                "OnlineSecurity": request.form['OnlineSecurity'],
                "OnlineBackup": request.form['OnlineBackup'],
                "DeviceProtection": request.form['DeviceProtection'],
                "TechSupport": request.form['TechSupport'],
                "StreamingTV": request.form['StreamingTV'],
                "StreamingMovies": request.form['StreamingMovies'],
                "Contract": request.form['Contract'],
                "PaperlessBilling": request.form['PaperlessBilling'],
                "PaymentMethod": request.form['PaymentMethod'],
                "MonthlyCharges": float(request.form['MonthlyCharges']),
                "TotalCharges": request.form['TotalCharges']  # Handle as string first
            }

            # Preprocess the data to match training format
            df_processed = preprocessor.preprocess_data(data)
            
            # Make prediction
            pipeline = PredictionPipeline()
            result = pipeline.predict(df_processed)

            # Calculate risk percentage (assuming binary classification)
            risk_percentage = int(result[0] * 100) if result[0] == 1 else int((1 - result[0]) * 100)
            
            return render_template('result.html', 
                                 prediction=int(result[0]),
                                 customer_data=data)

        except Exception as e:
            error_message = f"Prediction failed: {str(e)}"
            return render_template('error.html', error=error_message)

    return render_template('predict.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error="Internal server error occurred")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
