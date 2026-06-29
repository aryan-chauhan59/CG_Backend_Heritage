# Q4 Prime Numbers Between 1 and N.



N = int(input("Enter the value of N: "))

print(f"Prime numbers between 1 and {N} are:")

for num in range(2, N + 1):
    is_prime = True      
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  
            break             
    if is_prime == True:
        print(num, end=" ")  
print()