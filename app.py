from flask import Flask, render_template, url_for, request
from functions import Mifflin, Katch, your_tdee, all_tdees
# source env/bin/activate

app = Flask(__name__)


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
    activity_lvl = request.form.get('activity_lvl', 2)
    if body_fat == '':
        bmr = int((Mifflin(mass, height, age, sex)))
    else:
        bmr = int((Katch(mass, body_fat)))
    all_activity = []
    all_activity = all_tdees(bmr)
    return render_template('index.html', bmr=bmr, all_activity=all_activity)


if __name__ == "__main__":
    app.run(debug=True)
