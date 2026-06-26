# Q15 Find the missing number from an array containing numbers 1 to N.

def missingNumber(nums):
    
    N = len(nums) + 1
    expected_sum = N * (N + 1) // 2  
    actual_sum = sum(nums)
    return expected_sum - actual_sum