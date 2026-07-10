# QUICK SORT IMPLEMENTATION --
# Time Complexity:
# Best: O(n log n)
# Average: O(n log n)
# Worst: O(n^2) 

def quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
        temp = arr[i + 1]
        arr[i + 1] = arr[high]
        arr[high] = temp
        
        partition_index = i + 1
        print("Quick sort placed pivot", pivot, "-> Array state:", arr)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)      
    return arr
user_input = input("Enter numbers separated: ")
string_list = user_input.split()
original_list = []
for item in string_list:
    original_list.append(int(item))
print("\nQuick Sort")
quick_list = original_list.copy()
quick_sort(quick_list, 0, len(quick_list) - 1)

# OUTPUT :

# Enter numbers separated: 5 7 8 3 2

# Quick Sort
# Quick sort placed pivot 2 -> Array state: [2, 7, 8, 3, 5]
# Quick sort placed pivot 5 -> Array state: [2, 3, 5, 7, 8]
# Quick sort placed pivot 8 -> Array state: [2, 3, 5, 7, 8]