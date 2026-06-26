# Office Attendance Report Program


print("Office Attendance Report")

emp_name = input("Enter Employee Name: ")
total_days = int(input("Enter Total Working Days: "))
days_present = int(input("Enter Days Present: "))

days_absent = total_days - days_present
attendance_percentage = (days_present / total_days) * 100

print("\nAttendance Summary")
print(f"Employee: {emp_name}")
print(f"Total Working Days: {total_days}")
print(f"Days Present: {days_present}")
print(f"Days Absent: {days_absent}")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")