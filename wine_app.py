# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 12:24:26 2025

@author: katki
"""

from flask import Flask, render_template, request
import numpy as np
import pickle

#Loading my trained model
model = pickle.load(open('wine_model.pkl', 'rb'))

#Creating the Flask app
app = Flask(__name__)

#Home route
@app.route('/')
def home():
    return render_template('wine_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_values = [float(x) for x in request.form.values()]
        features = np.array([input_values])
        prediction = model.predict(features)
        return render_template('wine_form.html', prediction_text=f'Predicted wine class: {prediction[0]}')
    except Exception as e:
        return render_template('wine_form.html', prediction_text=f'Error: {str(e)}')
    
if __name__ == '__main__':
    app.run(debug=True)
    
