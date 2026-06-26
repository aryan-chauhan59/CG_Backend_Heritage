# 1. Employee Salary Breakdown Calculator Take employee name, basic salary, HRA %, and Bonus % as input.
# Calculate:HRA Amount ,Bonus Amount,Gross Salary,
# Display the result using formatted f-strings.


print("Employee Salary Calculator")

name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
hra_percent = float(input("Enter HRA percentage: "))
bonus_percent = float(input("Enter Bonus percentage: "))

hra_amount = (hra_percent / 100) * basic_salary
bonus_amount = (bonus_percent / 100) * basic_salary
gross_salary = basic_salary + hra_amount + bonus_amount

print("\nSalary Breakdown ")
print(f"Employee Name: {name}")
print(f"Basic Salary: ${basic_salary:.2f}")
print(f"HRA Amount: ${hra_amount:.2f}")
print(f"Bonus Amount: ${bonus_amount:.2f}")
print(f"Gross Salary: ${gross_salary:.2f}")