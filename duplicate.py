# Q16 Find the duplicate number in an array containing N+1 integers.

numbers = list(map(int, input("Array: ").split()))
seen_numbers = set()
duplicate = -1

for current_number in numbers:
    if current_number in seen_numbers:
        duplicate = current_number
        break
    seen_numbers.add(current_number)

print(duplicate)

