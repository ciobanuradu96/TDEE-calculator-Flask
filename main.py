#Katch-McArdle Equation if body fat prcentage is added
"""
Katch = 370 + (21.6 * LBM)
where LBM is lean body mass
"""
def Katch(lbm):
    return (370 + 21.6*lbm)
#Mifflin-St Jeor Equation
'''
Mifflin = (10.m + 6.25h - 5.0a) + s
m is mass in kg, h is height in cm, a is age in years, s is +5 for males and -151 for females
'''
def Mifflin(mass,height,age,sex):
    if sex=='male':
        s=5
    else: s=-151
    return(((10*mass)+(6.25*height)-(5*age))+s)

#Indexes
body_fat=""
mass=float(input("Enter your bodyweight in kg "))
height=int(input("Enter your height in cm "))
age=int(input("Enter your age "))
sex=input("Enter your gender ")
body_fat=input("Enter your body fat % (optional)")

if body_fat!="":
    lbm=(mass-(mass*(float(body_fat)*0.01))) #Lean Body Mass = Body Weight - (Body Weight * Body Fat %)
    print("Your LBM is:", lbm)
    print("Your basal metabolic rate is:", Katch(lbm))

print("Your basal metabolic rate is:",Mifflin(mass,height,age,sex))
