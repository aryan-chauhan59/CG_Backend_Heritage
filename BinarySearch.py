# Binary Search Implementation in Python

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

user_input = input("Enter sorted numbers separated: ")
string_list = user_input.split()

number_list = []
for item in string_list:
    number_list.append(int(item))

target_val = int(input("Enter the number want to find: "))

index = binary_search(number_list, target_val)

if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found in the list.")

# OUTPUT :

# Enter sorted numbers separated: 4 6 8 3 5 9
# Enter the number want to find: 5
# Target not found in the list.