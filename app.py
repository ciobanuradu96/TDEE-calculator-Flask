from flask import Flask, render_template, url_for, request
from time import ctime
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome


def Mifflin(mass, height, age, sex):
    if sex == 'male':
        s = 5
    else:
        s = -151
    return(((10*float(mass))+(6.25*int(height))-(5*int(age)))+s)


def Katch(mass, body_fat):
    lbm = (float(mass)-(float(mass)*(int(body_fat)*0.01)))
    return (370 + 21.6*lbm)


app = Flask(__name__)
Bootstrap(app)
fa = FontAwesome(app)


@app.route('/')
def index():
    return render_template('index.html', time=ctime())


@app.route('/', methods=["GET", "POST"])
def form_post():
    mass = request.form['mass']
    height = request.form['height']
    age = request.form['age']
    sex = request.form['sex']
    body_fat = request.form['body_fat']

    if body_fat == '':
        my_result = (Mifflin(mass, height, age, sex))
        return render_template('index.html', result=my_result)
    else:
        my_result = (Katch(mass, body_fat))
        return render_template('index.html', result=my_result)


if __name__ == "__main__":
    app.run(debug=True)
