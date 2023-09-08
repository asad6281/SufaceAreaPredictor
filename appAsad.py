from flask import Flask, render_template, request, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

app = Flask(__name__)

# Load the best model
model = load('PolyReg_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    radius = float(request.form['radius'])
    height = float(request.form['height'])
    X = np.column_stack((radius, height))
    poly = PolynomialFeatures(degree=2)
    X1 = poly.fit_transform(X)

    # predict
    prediction = model.predict(X1)
    return render_template('index.html', prediction=f'Surface Area: {prediction[0]:.2f}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

