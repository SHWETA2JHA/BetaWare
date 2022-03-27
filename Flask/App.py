# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import requests
import config
import pickle
import io



# Loading crop recommendation model

crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))



app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Betaware - Home'
    return render_template('agriculture1.html', title=title)

# render crop recommendation form page


@ app.route('/news-single.html')
def crop_recommend():
    title = 'Betaware - Crop Recommendation'
    return render_template('news-single.html', title=title)



@ app.route('/news-single.html', methods=['POST'])
def crop_prediction():
    title = 'Betaware - Crop Recommendation'
    try:
        if request.method == 'POST':
            N = int(request.form['nitrogen'])
            P = int(request.form['phosphorous'])
            K = int(request.form['pottasium'])
            ph = float(request.form['ph'])
            humidity = float(request.form['humidity'])
            temperature = float(request.form['temperature'])
            rainfall = float(request.form['rainfall'])
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]
            return render_template('crop_result.html', prediction=final_prediction, title=title)
    except Exception as e:
        print(e)
        return e


if __name__ == '__main__':
    app.run(debug=False)