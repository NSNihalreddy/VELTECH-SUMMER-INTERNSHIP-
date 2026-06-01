weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))

height = height / 100

BMI = weight / (height * height)

if BMI < 18.5:
    print("Underweight")
elif BMI <= 24.9:
    print("Normal")
else:
    print("Overweight")
