# Q2 Find all pairs in a list whose sum equals a target value.

a = list(map(int, input("Array: ").split()))
b = int(input("Target: "))
c = []

for d in range(len(a)):
    for e in range(d + 1, len(a)):
        if a[d] + a[e] == b:
            c.append((a[d], a[e]))

print(c)