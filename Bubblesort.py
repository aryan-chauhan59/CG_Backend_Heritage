# BUBBLE SORT IMPLEMENTATION --

# Time Complexity:
# Best: O(n)    
# Average: O(n^2)
# Worst: O(n^2)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        print("Bubble sort ", i + 1, ":", arr)
    return arr

user_input = input("Enter numbers separated: ")
string_list = user_input.split()

original_list = []
for item in string_list:
    original_list.append(int(item))

print("\nBubble Sort")
sorted_list = bubble_sort(original_list.copy())