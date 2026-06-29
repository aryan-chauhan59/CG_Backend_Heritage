# Q5 Voting Eligibility Management System
# Create a program that:
# Takes name and age as input
# Checks whether the person is eligible to vote
# Stores eligible and non-eligible users in separate lists
# Displays the final report
# Sample Output
#Enter Name: Ankan
#Enter Age: 20
#Ankan is eligible to vote.

name = input("Enter Name: ")
age = int(input("Enter Age: "))

if age >= 18:
    print(f"{name} is eligible to vote.")
else:
    print(f"{name} is not eligible to vote.")