# Given a sorted salary list, recursively implement Binary Search.

def recursive_binary_search(salaries, target, left, right):
    if left > right:
        return "Salary not found"
        
    mid = (left + right) // 2
    
    if salaries[mid] == target:
        return f"Salary {target} found at index {mid}"
        
    elif salaries[mid] < target:
        return recursive_binary_search(salaries, target, mid + 1, right)
        
    else:
        return recursive_binary_search(salaries, target, left, mid - 1)

salaries = [40000, 55000, 60000, 75000, 90000]
print(recursive_binary_search(salaries, 75000, 0, len(salaries) - 1))