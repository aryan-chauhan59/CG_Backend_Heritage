# Q1 Find the maximum sum subarray (Kadane’s Algorithm).

a = list(map(int, input("Array: ").split()))
b = a[0]
c = a[0]

for d in a[1:]:
    b = max(d, b + d)
    c = max(c, b)

print(c)