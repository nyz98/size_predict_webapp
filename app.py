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


        input_variables = pd.DataFrame([[weight, age, height]], columns=['weight', 'age', 'height'], dtype=float)

        prediction = model.predict(input_variables)[0]

        # Convert numerical prediction to categorical
        if prediction >= 6.50:
            pred = "XXXL"
        elif prediction >= 6.00:
            pred = "XXL"
        elif prediction >= 5.30:
            pred = "XL"
        elif prediction >= 4.10:
            pred = "L"
        elif prediction >= 3.40:
            pred = "M"
        elif prediction >= 2.70:
            pred = "S"
        elif prediction >= 2.00:
            pred = "XS"
        else:
            pred = "XXS"

        return render_template('home.html',
                                original_input=
                                {'Height':height,
                                'Weight':weight,
                                'Age':age},
                                result=pred,
                                )

if __name__ == '__main__':
    app.run()