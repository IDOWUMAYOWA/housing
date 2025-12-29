import pickle
from flask import Flask, request, jsonify,app,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
reg_model = pickle.load(open('/home/ims24/housing/linear_regression_model.pkl', 'rb'))
scaler = pickle.load(open('/home/ims24/housing/scaler.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    tranform_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    prediction = reg_model.predict(tranform_data)
    print(prediction[0])
    return jsonify(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
