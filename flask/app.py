from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns   
from pivottablejs import pivot_ui
import datetime
from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

import joblib
import json
import requests

app = Flask(__name__) 

@app.route('/')
def index(): 
    return render_template('index.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,7)
    loaded_model = joblib.load('final_model.sav')
    result = loaded_model.predict(to_predict)
    return result[0]

# @app.route('/model', methods=['POST'])
# def model():
#     inputs = request.get_json()
#     prediction = np.array2string(loaded_model.predict([inputs])
#     return jsonify(prediction)

@app.route('/result',methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list) 
    return render_template("result", prediction=result)

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

url = 'http://localhost:5000/results'
r = requests.post(url)

print(r.json())
