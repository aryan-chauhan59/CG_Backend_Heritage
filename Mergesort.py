# MERGE SORT ---
# Time Complexity:
# Best: O(n log n)
# Average: O(n log n)
# Worst: O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0 # Index for left_half
        j = 0 # Index for right_half
        k = 0 # Index for main array

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
        print("Merge sort:", arr)
    return arr
user_input = input("Enter numbers separated: ")
string_list = user_input.split()

original_list = []
for item in string_list:
    original_list.append(int(item))

print("\nMerge Sort")
merge_sort(original_list.copy())

# OUTPUT:

# Enter numbers separated: 5 7 8 3 2

#Merge Sort
#Merge sort: [5, 7]
#Merge sort: [2, 3]
#Merge sort: [2, 3, 8]
#Merge sort: [2, 3, 5, 7, 8]