from flask import Flask, render_template, request
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

        ram = int(request.form['rm'])
        pw = int(request.form['pw'])
        ph = int(request.form['ph'])
        bc = int(request.form['bc'])
        ints = int(request.form['is'])

        data = [[ram, bc, pw, ph, ints]]
        print(data)
        res = model.predict(data)
        return render_template('home.html', result=res)


if __name__ == "__main__":
    app.run(debug=True)
