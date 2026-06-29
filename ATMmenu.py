# Q3  ATM Menu Using Match-Case
#Options:Balance Check,Deposit,Withdraw,Exit
#Implement using match-case.

print("Welcome to the ATM!")

while True:
    print("\nOptions:")
    print("1. Balance Check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is 1500")

    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        print(f"{amount} has been deposited")

    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        print(f"{amount} has been withdrawn")

    elif choice == "4":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice. Please try again.")


