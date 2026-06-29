class LinkedList:

    def delete_by_value(self, value):
        if self.head is None:
            raise ValueError('Cannot delete from empty list')
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next
        raise ValueError(f'{value} not found in list')

    def delete_at_position(self, position):
        if position < 0 or position >= self._size:
            raise IndexError(f'Position {position} out of range')
        if position == 0:
            self.head = self.head.next
            self._size -= 1
            return
        current = self.head
        for _ in range(position - 1):
            current = current.next
        current.next = current.next.next
        self._size -= 1