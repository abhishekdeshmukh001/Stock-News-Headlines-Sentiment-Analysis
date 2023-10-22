# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 14:25:50 2023

@author: Shahu
"""

import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle

# Load the Decision Tree model and CountVectorizer object
filename = 'stock-sentiment-dt-model.pkl'
classifer = pickle.load(open(filename, 'rb'))
cv = pickle.load(open('cv-transform.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method=='POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        
        my_prediction = classifer.predict(vect)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)