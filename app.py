import pickle
from flask import Flask, request, jsonify,app,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
reg_model = pickle.load(open('/linear_regression_model.pkl', 'rb'))
scaler = pickle.load(open('/scaler.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_test', methods=['POST'])
def predict_test():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    tranform_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    prediction = reg_model.predictt(tranform_data)
    print(prediction[0])
    return jsonify(prediction[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1, -1))
    print(final_input)
    prediction = reg_model.predict(final_input)[0]
    return render_template('home.html', prediction_text=f'The predicted housing price is {prediction}')
   



if __name__ == '__main__':
    app.run(debug=True)
