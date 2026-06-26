# Q14

a = list(map(int, input("Array: ").split()))
b = int(input("K: "))

if len(a) > 0:
    b = b % len(a)
    a[:] = a[-b:] + a[:-b]

print(a)