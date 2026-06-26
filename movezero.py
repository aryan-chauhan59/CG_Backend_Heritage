# Q19 Move all zeros to the end while maintaining order.

a = list(map(int, input("Array: ").split()))
b = 0

for c in range(len(a)):
    if a[c] != 0:
        a[b], a[c] = a[c], a[b]
        b = b + 1

print(a)