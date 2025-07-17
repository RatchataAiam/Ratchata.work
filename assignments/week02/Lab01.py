"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
W = float(input("Weight: "))
H = float(input("Height: "))
HM = H / 100
BMI = W / (HM ** 2)
print("Your BMI: ",BMI)

if BMI < 18.5:
    print("You'r Underweight")
elif  BMI >=18.5 and BMI <=24.9:
    print("You'r Normal weight")

elif BMI >=25.0 and BMI <=29.9:
    print("You'r Overweight")

elif BMI >=30:
    print("You'r Obese")