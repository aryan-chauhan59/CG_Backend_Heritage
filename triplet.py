# Q13 Find all triplets whose sum equals zero.

a = list(map(int, input("Array: ").split()))
a.sort()
b = []

for c in range(len(a) - 2):
    if c > 0 and a[c] == a[c - 1]:
        continue
    d = c + 1
    e = len(a) - 1
    while d < e:
        f = a[c] + a[d] + a[e]
        if f == 0:
            b.append([a[c], a[d], a[e]])
            d = d + 1
            while d < e and a[d] == a[d - 1]:
                d = d + 1
        elif f < 0:
            d = d + 1
        else:
            e = e - 1

print(b)