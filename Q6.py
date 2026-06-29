# Employee Tax Estimator


print("Employee Tax Estimator")

emp_name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
monthly_salary = float(input("Enter Monthly Salary: $"))
tax_percentage = float(input("Enter Tax Percentage: "))

annual_salary = monthly_salary * 12
annual_tax = (tax_percentage / 100) * annual_salary
net_annual_salary = annual_salary - annual_tax

print("\nProfessional Salary Report")
print(f"Employee Name: {emp_name} (ID: {emp_id})")
print(f"Annual Gross Salary: ${annual_salary:.2f}")
print(f"Estimated Annual Tax: ${annual_tax:.2f}")
print(f"Net Annual Salary: ${net_annual_salary:.2f}")