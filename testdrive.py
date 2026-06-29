# Test drive for linked list implementation

from deletion import LinkedList

ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
print('After inserting 10, 20, 30 at end:')
ll.traverse()

ll.insert_at_beginning(5)
print('After inserting 5 at beginning:')
ll.traverse()

ll.insert_at_position(15, 2)
print('After inserting 15 at position 2:')
ll.traverse()

print(f'Length: {ll.length()}')

print(f'Search 15: position {ll.search(15)}')
print(f'Search 99: position {ll.search(99)}')

ll.delete_by_value(15)
print('After deleting 15:')
ll.traverse()

ll.delete_at_position(0)
print('After deleting at position 0:')
ll.traverse()

ll.reverse()
print('After reversing:')
ll.traverse()