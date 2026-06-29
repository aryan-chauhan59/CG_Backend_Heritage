# Q17 Merge two sorted arrays into a single sorted array.

a = list(map(int, input("Array 1: ").split()))
b = list(map(int, input("Array 2: ").split()))

c = a + b
c.sort()

print(c)