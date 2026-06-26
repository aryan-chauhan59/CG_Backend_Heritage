# Q18 Find the longest consecutive sequence in an unsorted array.

a = list(map(int, input("Array: ").split()))
b = set(a)
c = 0

for d in b:
    if d - 1 not in b:
        e = d
        f = 1
        while e + 1 in b:
            e = e + 1
            f = f + 1
        if f > c:
            c = f

print(c)