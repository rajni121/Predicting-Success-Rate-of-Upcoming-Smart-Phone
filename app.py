from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('random_forest_model.pkl')  # Load your saved model
scaler = joblib.load('scaler.pkl')  # Load your saved scaler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('templates/index.html')  # This is the main page where the input form will be

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    features = [
        float(request.form['Price']),
        float(request.form['RAM']),
        float(request.form['ROM']),
        float(request.form['Height']),
        float(request.form['Width']),
        float(request.form['Main_Cam']),
        float(request.form['Extra_Cam']),
        float(request.form['Front_Cam']),
        float(request.form['Battery']),
        int(request.form['Color_Black',0]),
        int(request.form['Color_White',0]),
        int(request.form['Processor_MediaTek']),
        int(request.form['Processor_Qualcomm']),
        int(request.form['Processor_Unknown'])
    ]

    # Scale the features
    features_scaled = scaler.transform([features])

    # Make prediction
    prediction = model.predict(features_scaled)

    return jsonify({'predicted_review': prediction[0]})
if __name__ == '__main__':
    app.run(debug=True)
