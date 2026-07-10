# Linear Search Implementation in Python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

user_input = input("Enter numbers separated: ")
string_list = user_input.split()

number_list = []
for item in string_list:
    number_list.append(int(item))

target_val = int(input("Enter the number want to find: "))

index = linear_search(number_list, target_val)

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found in the list.")

# OUTPUT :

# Enter numbers separated: 4 6 8 3 5 9
# Enter the number want to find: 8
# Target found at index: 2