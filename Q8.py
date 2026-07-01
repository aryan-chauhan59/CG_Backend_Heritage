# Analyze the time and space complexity of finding the maximum value in a list.

def find_maximum(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    
    for num in numbers:
        if num > max_val:
            max_val = num 
            
    return max_val

scores = [45, 12, 89, 33, 91, 7]
print(f"The maximum value is: {find_maximum(scores)}")