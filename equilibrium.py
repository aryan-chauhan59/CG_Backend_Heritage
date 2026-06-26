# Q20 Find the equilibrium index of an array.

numbers = list(map(int, input("Array: ").split()))
right_sum = sum(numbers)
left_sum = 0
equilibrium_index = -1

for i in range(len(numbers)):
    right_sum = right_sum - numbers[i]
    
    if left_sum == right_sum:
        equilibrium_index = i
        break
        
    left_sum = left_sum + numbers[i]

print(equilibrium_index)


# The logic is: in the array we are taking, 
# if the sum of the right side and left side is the same, 
# then it's fine, otherwise it will show -1.