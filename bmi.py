# Q6 Build a simple BMI Calculator.

height = int(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")