# INSERTION SORT IMPLEMENTATION --
# Time Complexity:
# Best: O(n)     
# Average: O(n^2)
# Worst: O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print("Insertion sort", i, ":", arr)
    return arr
user_input = input("Enter numbers separated: ")
string_list = user_input.split()

original_list = []
for item in string_list:
    original_list.append(int(item))

print("\ninsertion Sort")
insertion_sort(original_list.copy())