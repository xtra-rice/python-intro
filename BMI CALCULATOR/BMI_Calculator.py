import math

#BMI Calculator
name1 = "Julia"
height1 = 2
weight1 = 90

name2 = "Erice"
height2 = 1.8
weight2 = 70

name3 = "Amarah"
height3 = 2.5
weight3 = 160


def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi <= 24.9:
        bmi_category = "Healthy weight range"
    elif bmi <=29.9:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"
    return f"{bmi:.2f}", bmi_category
    

bmi_result1 = bmi_calculator(name1, height1, weight1)
bmi_result2 = bmi_calculator(name2, height2, weight2)
bmi_result3 = bmi_calculator(name3, height3, weight3)
bmi, bmi_category = bmi_result1 
print(f"{name1}'s BMI Category is: {bmi_result1}")
print(f"{name2}'s BMI Category is: {bmi_result2}")
print(f"{name3}'s BMI Category is: {bmi_result3}")
    

