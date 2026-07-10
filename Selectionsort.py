# SELECTION SORT IMPLEMENTATION --
# Time Complexity:
# Best: O(n^2)
# Average: O(n^2)
# Worst: O(n^2)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
        print("Selection sort", i + 1, ":", arr)
    return arr

user_input = input("Enter numbers separated: ")
string_list = user_input.split()

original_list = []
for item in string_list:
    original_list.append(int(item))

print("\nSelection Sort")
selection_sort(original_list.copy())