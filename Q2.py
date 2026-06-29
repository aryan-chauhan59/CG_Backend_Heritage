# 2. Smart Age Calculator Take birth year as input.
# Calculate:Current Age,Age after 10 years,Age before 5 years
# Display all results in a formatted report.

import datetime

print("Smart Age Calculator")

birth_year = int(input("Enter your birth year: "))

current_year = datetime.date.today().year

current_age = current_year - birth_year
age_after_10 = current_age + 10
age_before_5 = current_age - 5

print("\nAge Report")
print(f"Current Age: {current_age} years old")
print(f"Age after 10 years: {age_after_10} years old")
print(f"Age 5 years ago: {age_before_5} years old")