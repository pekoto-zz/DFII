from typing import Any


class Node:

    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return self.val

    def __repr__(self):
        return repr(self.val)


class DoublyLinkedList:
    """ A doubly linked list. We could also call this a queue/deque.

    deque = "deck", double-ended queue.

    * Add to head/tail: O(1)
    * Pop head/tail: O(1)
    * Remove value: O(n)

    Uses:
        * Implement stack or queue.
        * No need to resize when adding or removing.
    """
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self.size = 0

    def add_to_head(self, val: Any) -> None:
        """Adds an item to the start of the queue.

        1. Save the previous head.
        2. If the tail is null, set head = tail.
        3. Else, set previous head and current head to link to each other.

        Time: O(1)
        Space: O(1)

        :param val: The item to add.
        :return: None
        """
        previous_head = self._head
        self._head = Node(val)

        if not self._tail:
            self._tail = self._head
        else:
            self._head.next = previous_head
            previous_head.prev = self._head

        self.size += 1

    def add_to_tail(self, val: Any) -> None:
        """Adds an item to the end of the queue.

        1. Save the previous tail
        2. Create a new tail
        3. If the list is empty, head = tail
        4. Else, set the previous tail next and current tail previous

        Time: O(1)
        Space: O(1)

        :param val: The item to add.
        :return: None
        """
        previous_tail = self._tail
        self._tail = Node(val)

        if not self._head:  # 1-item list/queue
            self._head = self._tail
        else:
            previous_tail.next = self._tail
            self._tail.prev = previous_tail

        self.size += 1

    def pop_head(self) -> Any:
        """Removes and returns the head.

        1. Save the value at head.
        2. Set head = head.next
        3. If new head empty, set the tail empty too.

        Time: O(1)
        Space: O(1)

        :return: The value at head.
        """
        if not self._head:
            raise Exception('List is empty')

        val = self._head.val
        self._head = self._head.next
        self.size -= 1

        if not self._head:  # We had a len(1) queue.
            self._tail = None

        return val

    def pop_tail(self) -> Any:
        """Removes and returns the tail.

        1. Save the value at tail.
        2. Set the tail to be tail previous.
        3. If the tail is null, set head null too.

        Time: O(1)
        Space: O(1)

        :return: The value at tail.
        """
        if not self._tail:
            raise Exception('List is empty')

        val = self._tail.val
        self._tail = self._tail.prev
        self.size -= 1

        if not self._tail:  # We had a len(1) queue.
            self._head = None

        return val

    def remove_val(self, val: Any) -> None:
        """Removes a value from the queue.

        1. Iterate while current node exists and doesn't equal value.
        2. If current node == None, the value wasn't found.
        3. If current node is head or tail, pop head or pop tail
        4. Else set the previous node's next to the current node's next.

        Time: O(n)
        Space: O(1)

        :param val: Value to remove.
        :return: None.
        """
        if not self._head:
            raise KeyError('Value not found (list empty)')

        current_node = self._head

        while current_node and current_node.val != val:
            current_node = current_node.next

        if not current_node:
            raise KeyError('Value not found')

        if current_node is self._head:
            self.pop_head()
        elif current_node is self._tail:
            self.pop_tail()
        else:
            current_node.prev.next = current_node.next
            self.size -= 1

    def reverse(self) -> None:
        """Reverses the queue.

        1. Set up pointers for previous, current, and next. Save old head.
        2. While current is not null:
            2.1 Set next to next
            2.2 Set current.prev to next
            2.3 Set current.next to prev
            2.4 Update the pointers: previous = current, current = next
        3. Finally, set head to previous, and tail to old head that you saved.

        Time: O(n)
        Space: O(1)

        :return: None.
        """
        if self.size <= 1:
            return

        previous = None
        current = self._head
        next_node = None

        old_head = self._head

        while current:
            next_node = current.next
            current.prev = next_node
            current.next = previous

            # Update pointers
            previous = current
            current = next_node

        self._tail = old_head
        self._head = previous

    def is_empty(self) -> bool:
        return self.size == 0

    def __iter__(self):
        self.current = self._head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration

        val = self.current
        self.current = self.current.next
        return val
