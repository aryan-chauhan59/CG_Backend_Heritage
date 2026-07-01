# Implement Binary Search to find a student in a sorted list of roll numbers.

def binary_search(roll_numbers, target):
    left = 0
    right = len(roll_numbers) - 1
    
    while left <= right:
        mid = (left + right) // 2 
        
        if roll_numbers[mid] == target:
            return f"Student found at index {mid}"
        elif roll_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return "Student not found"

sorted_rolls = [12, 25, 34, 46, 58, 62, 79]
print(binary_search(sorted_rolls, 46))