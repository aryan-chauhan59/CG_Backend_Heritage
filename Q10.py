# Find whether two numbers in a sorted list add up to a budget using Two-Pointer.

def check_budget_sum(expenses, budget):
    left = 0
    right = len(expenses) - 1
    
    while left < right:
        current_sum = expenses[left] + expenses[right]
        
        if current_sum == budget:
            return f"Found match: {expenses[left]} + {expenses[right]} = {budget}"
            
        elif current_sum < budget:
            left += 1
            
        else:
            right -= 1
            
    return "No two expenses add up to the exact budget."

sorted_expenses = [10, 25, 30, 45, 60, 80]
print(check_budget_sum(sorted_expenses, 70))