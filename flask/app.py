from flask import Flask, render_template, request, jsonify
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import joblib
import json
import requests

app = Flask(__name__) 
loaded_model = joblib.load('less_feat.pkl')


@app.route('/') 
def index(): 
    return render_template('index.html')    


@app.route('/', methods=["POST"])
def model(): 
    inputs = []
    for idx in ['race', 'sex', 'ms', 'adjinc', 'educ', 'hhnum', 'pob', 'hitype']:
        input = request.form.get(idx)
        inputs.append(input)
    results = loaded_model.predict([inputs])
    results = str(results)
    return f'Based on 2002 mortality data, you can expect to die at age {results}'

# @app.route('/result')
# def result(): 
#     return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)