from collections import deque

queue = deque()

user_input = input("Enter customer names separated: ")
customers = user_input.split()

for person in customers:
    queue.append(person)
    print("Someone joined:", person)
    print("Current Queue state:", list(queue))

print("\nStarting to serve customers...")

while len(queue) > 0:
    served = queue.popleft()
    print("Now serving:", served)
    print("Current Queue state:", list(queue))

# OUTPUT:

# Enter customer names separated: Aryan Yash Bikram
# Someone joined: Aryan
# Current Queue state: ['Aryan']
# Someone joined: Yash
# Current Queue state: ['Aryan', 'Yash']
# Someone joined: Bikram
# Current Queue state: ['Aryan', 'Yash', 'Bikram']

# Starting to serve customers...
# Now serving: Aryan
# Current Queue state: ['Yash', 'Bikram']
# Now serving: Yash
# Current Queue state: ['Bikram']
# Now serving: Bikram
# Current Queue state: []