"""
Assignement 1 Baby Steps Control Structures
"""
# =========================
# Welcome to Assignment-1
# =========================

print("Welcome to Assignment-1")

# =========================
Num1= 10
Num2= 30
Add= Num1 + Num2
print(Num1)
print(Num2)
print(Add)
# =========================

#Body Mass Index


Height = float(input("Enter your height in meters: "))
Weight = float(input("Enter your weight in kilograms: "))
BMI = Weight / (Height ** 2)

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal weight")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obesity")