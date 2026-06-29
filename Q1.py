# Complete linked list implementation with Base Structure, Utilities, and Insertion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def insert_at_position(self, data, position):
        if position < 0 or position > self._size:
            raise IndexError(f'Position {position} out of range')
        if position == 0:
            return self.insert_at_beginning(data)
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def length(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def traverse(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(' → '.join(elements) + ' → None')

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' → '.join(elements) + ' → None'

    def __len__(self):
        return self._size
