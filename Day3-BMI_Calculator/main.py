print("Welcome to Wizard's BMI Calculator!")

height = float(input("Please enter your height in m. (Eg. 1.85) m: "))
weight = float(input("Please enter your weight in kg: "))
bmi = round(weight / (height ** 2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

