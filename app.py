from flask import Flask, render_template, url_for, request, redirect,session
from functions import Mifflin, Katch, your_tdee, all_tdees,bmi
import sqlalchemy
# source env/bin/activate

app = Flask(__name__)
#app.secret_key="test"



@app.route('/index', methods=["GET"])
def form_post():
    # if request.method=="POST":
    #     #mass = request.form['mass']
    #     session["mass"]=mass
    #     height = request.form['height']
    #     age = request.form['age']
    #     sex = request.form['sex']
    #     body_fat = request.form['body_fat']
    #     activity_lvl = request.form.get('activity_lvl', 2)
    #     return redirect(url_for('results.html'))
    return render_template('index.html')

@app.route('/results', methods=[ "POST"])
def results():
    mass =float(request.form['mass'])
    height = int(request.form['height'])
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
    test=bmi(mass,height)
    return render_template('results.html', bmr=bmr, all_activity=all_activity, test=test)


if __name__ == "__main__":
    app.run(debug=True)
