# Q11 Student Management System using Lists and Dictionaries.

students = {}
while True:
    name = input("Enter student name: ")
    if name.lower() == 'exit':
        break
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    students[name] = {'age': age, 'grade': grade}

print("\nStudent Information:")
for name, info in students.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")