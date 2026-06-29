# Q1 Student Grade Classifier Take marks as input and classify:
#A (90+)
#B (80-89)
#C (70-79)
#D (60-69)
#F (<60)

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")