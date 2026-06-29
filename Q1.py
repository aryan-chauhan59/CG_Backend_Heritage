# Combined example: linked list and stack implementation

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


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        if self.is_empty():
            return "Stack: [EMPTY]"
        return f"Stack [bottom→top]: {self._data}"


if __name__ == "__main__":
    book_stack = Stack()
    book_stack.push("Python Basics")
    book_stack.push("Data Structures")
    book_stack.push("Algorithms")
    book_stack.push("System Design")
    book_stack.push("Clean Code")

    print(book_stack)
    print(f'Total books stacked: {book_stack.size()}')
    print(f'Top book right now: {book_stack.peek()}')

    print('\n Removing books one by one (LIFO)')
    removed = book_stack.pop()
    print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}')

    removed = book_stack.pop()
    print(f'Removed: {removed:<20} | Stack size: {book_stack.size()}')

    print(f'\nRemaining: {book_stack}')
