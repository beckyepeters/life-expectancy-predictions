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

app = Flask(__name__) 

loaded_model = joblib.load('model_rf_age_adjusted_wonder.sav')

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict(): 
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='You can expect to die at the age of {}'.format(output))


def model(): 
    inputs = request.args
    results = loaded_model.predict([inputs['input_1']])
    answer = int(results)
    return answer

@app.route('/results',methods=['POST'])
def results(): 
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__": 
    app.run(debug=True)