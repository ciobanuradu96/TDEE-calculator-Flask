def Mifflin(mass, height, age, sex):
    if sex == 'male':
        s = 5
    else:
        s = -151
    return(((10*float(mass))+(6.25*int(height))-(5*int(age)))+s)


def Katch(mass, body_fat):
    lbm = (float(mass)-(float(mass)*(int(body_fat)*0.01)))
    return (370 + 21.6*lbm)


def your_tdee(bmr, activity_lvl):
    if activity_lvl == 0:
        return bmr*1.2
    elif activity_lvl == 1:
        return bmr*1.37
    elif activity_lvl == 2:
        return bmr*1.55
    elif activity_lvl == 3:
        return bmr*1.725
    else:
        return bmr*1.9


def all_tdees(bmr):
    all_tdees = []
    activity_rates = [1.2, 1.37, 1.55, 1.725, 1.9]
    for counter in range(0, 5):
        all_tdees.append(int(bmr*activity_rates[counter]))
    return all_tdees


def bmi(mass, height):
    return round(mass/pow((height/100), 2), 2)
