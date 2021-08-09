from setup.core import size_predict
from flask import Flask, render_template
import flask
import pickle
import pandas as pd
import xgboost

# Use pickle to load in the pre-trained model.
with open(f'model/size_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'GET':
        return render_template('home.html')

    if flask.request.method == 'POST':

        height = flask.request.form['height']
        weight = flask.request.form['weight']
        age = flask.request.form['age']

        bmi = float(weight) / (float(height)**2) * 10000
        input_variables = pd.DataFrame([[age, bmi]], columns=['age', 'bmi'], dtype=float)

        pred = size_predict(model, input_variables)

        return render_template('home.html',
                                original_input=
                                {'Height':height,
                                'Weight':weight,
                                'Age':age},
                                result=pred,
                                )

if __name__ == '__main__':
    app.run()