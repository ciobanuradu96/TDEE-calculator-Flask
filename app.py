from flask import Flask, render_template, url_for, request, redirect, session
from functions import Mifflin, Katch, your_tdee, all_tdees, bmi
# source env/bin/activate

app = Flask(__name__)


@app.route('/index', methods=["GET"])
def form_post():
    return render_template('index.html')


@app.route('/results', methods=["POST"])
def results():
    mass = float(request.form['mass'])
    height = int(request.form['height'])
    age = int(request.form['age'])
    sex = request.form['sex']
    body_fat = float(request.form['body_fat'])
    activity_lvl = int(request.form.get('activity_lvl'))
    if body_fat == '':
        bmr = round(Mifflin(mass, height, age, sex))
    else:
        bmr = round(Katch(mass, body_fat))
    all_activity = []
    all_activity = all_tdees(bmr)
    test = bmi(mass, height)
    tdee = round(your_tdee(bmr, activity_lvl))
    selected = activity_lvl
    return render_template('results.html', bmr=bmr, all_activity=all_activity, test=test, tdee=tdee, selected=selected)


if __name__ == "__main__":
    app.run(debug=True)
