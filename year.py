# Q9 Convert a given number of days into years, months, and days.

days = int(input("Enter the number of days: "))
years = days // 365
days = days % 365
months = days // 30
days = days % 30
print(f"Years: {years}, Months: {months}, Days: {days}")