def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

linear_index = linear_search(numbers)
if linear_index != -1:
    print("Linear Search:index", linear_index)
else:
    print("Linear Search: not found")

binary_index = binary_search(numbers)
if binary_index != -1:
    print("Binary Search:index", binary_index)
else:
    print("Binary Search:not found")