from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


data = []


@app.route('/pred', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        add = open('model.pkl', 'rb')
        model = pickle.load(add)

        ram = int(float(request.form['rm']))
        pw = int(float(request.form['pw']))
        ph = int(float(request.form['ph']))
        bc = int(float(request.form['bc']))
        ints = int(float(request.form['is']))

        data = [[ram, bc, pw, ph, ints]]
        r = model.predict(data)
        print(r)

        if r == 1:
            res = "Low Budget Device"
        if r == 2:
            res = "Mid Range Device"
        if r == 3:
            res = "High-end Device"

        return render_template('home.html', result=res)


if __name__ == "__main__":
    app.run(debug=True)
