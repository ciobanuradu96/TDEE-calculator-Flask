from flask import Blueprint, render_template, url_for, request, redirect, session
from website.functions import Mifflin, Katch, your_tdee, all_tdees, bmi

views = Blueprint('views', __name__)


@views.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@views.route('/results', methods=["POST"])
def result_page():
    mass = float(request.form['mass'])
    height = int(request.form['height'])
    age = int(request.form['age'])
    sex = request.form['sex']
    body_fat = request.form['body_fat']
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
    gender = sex
    return render_template('results.html', bmr=bmr, all_activity=all_activity, test=test, tdee=tdee, selected=selected, body_fat=body_fat, gender=gender)
