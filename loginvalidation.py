# Q2  Login Validation System Create a login system with:
#Username = admin
#Password = python123
#Maximum 3 attempts

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "aryan" and password == "lol1122":
        print("Login successful! Welcome")
        break  
    else:
        attempts = attempts - 1
        print(f"Incorrect password.You have {attempts} attempts left.\n")

if attempts == 0:
    print("Account locked. Maximum attempts reached.")