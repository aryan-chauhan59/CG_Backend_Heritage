# Student Percentage & grade analyzer



print("Student Grade Analyzer")

student_name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
history = float(input("Enter History marks: "))
art = float(input("Enter Art marks: "))

total_marks = math + science + english + history + art
percentage = (total_marks / 500) * 100

print("\nResult")
print(f"Student: {student_name}")
print(f"Total Marks: {total_marks:.2f} / 500")
print(f"Percentage: {percentage:.2f}%")