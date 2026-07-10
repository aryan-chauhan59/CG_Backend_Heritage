
height = float(input("Enter your height in meters (m): "))
weight = float(input("Enter your weight in kilograms (kg): "))

bmi = weight / (height ** 2)


print(f"Your BMI is: {bmi:.2f}")

if bmi < 18:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

# OUTPUT:

# Enter your height in meters (m): 170
# Enter your weight in kilograms (kg): 65
# Your BMI is: 2.23
# Category: Normal