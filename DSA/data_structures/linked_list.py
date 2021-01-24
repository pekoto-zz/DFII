from typing import Any


class Node:

    def __init__(self, val: Any = None) -> None:
        self.val = val
        self.next = None

    def __str__(self):
        return self.val


class LinkedList:
    """A singly linked list.

    Add: O(n)
    Remove: O(n)
    Lookup: O(n)

    Uses:
    * Implement stacks of queues
    * Adjacency list representation of graphs
    * Chained hashmap chain
    * No need to resize when growing/shrinking (more memory efficient)
    (Generally a doubly linked list will give better performance tho...)
    """

    def __init__(self) -> None:
        self._head = None
        self.size = 0

    def add_recursive(self, val: Any) -> None:
        """Adds an item to the list in a recursive manner.

        If the root is null, set it to be a new node.
        If the root is not null, recurse through the list
        until we hit a null node, at which point we'll add a new node
        and set as the previous node's next node.

        Example:
        1 > 2 --> add_recursive(3)
        1.next = add_recursive(2, 3)
        2.next = add_recursive(null, 3)
        return 3
        2.next = 3
        1.next = 2
        root = 1

        Time: O(n)
        Space: O(n) -- due to callstack growth

        :param val: The item to add.
        :return: None
        """
        self._head = self._add_recursive(self._head, val)
        self.size += 1

    def _add_recursive(self, node: Node, val: Any) -> Node:
        if not node:
            return Node(val)

        node.next = self._add_recursive(node.next, val)
        return node

    def add_iterative(self, val: Any) -> None:
        """Adds a value iteratively.

        Time: O(n)
        Space: O(1)

        :param val: The item to add
        :return: None
        """
        if not self._head:
            self._head = Node(val)
        else:
            new_node = self._head
            while new_node.next:
                new_node = new_node.next
            new_node.next = Node(val)

        self.size = self.size + 1

    def remove_recursive(self, val: Any) -> None:
        """Removes a value from the list recursively.

        If we hit a null node, throw a key error -- the value did not exist.
        If we find the value, set the previous node next to the next node.
        Otherwise, recurse to the next node.

        For example: 1->2->3->NULL, remove(3)

        1. Call with (1), doesn't match
        2. 1.next = remove(2, 3), doesn't match
        3. 2.next = remove(3, 3), matches
        3. set 2.next = 3.next == s.next = null
        4. left with 1->2->NULL

        Time: O(n)
        Space: O(n), due to callstack growth

        :param val: The item to remove
        :return: None
        """
        self._head = self._remove_recursive(self._head, val)

    def _remove_recursive(self, node: Node, val: Any) -> Node:
        if not node:
            raise KeyError('Value not found %s', val)

        if node.val == val:
            self.size -= 1
            return node.next

        node.next = self._remove_recursive(node.next, val)

        return node

    def remove_iterative(self, val: Any) -> None:
        """Removes a node in an iterative manner.

        For this we need to have more edge-case checking.

        1. If the head is null, raise a KeyError.
        2. If the head matches, just set head = head.next.
        3. Else, set current node.
           While current_node.next != val != val, loop
           If the next node is null, key error.
           Otherwise set node.next = node.next.next

        Time: O(n)
        Space: O(1)

        :param val: The value of the thing to remove.
        :return: None
        """
        if not self._head:
            raise KeyError('Value not found %s', val)

        # If it matches and this is the head, set head to be node.next
        if self._head.val == val:
            self._head = self._head.next
            self.size -= 1
        else:
            current_node = self._head

            while current_node.next and current_node.next.val != val:
                current_node = current_node.next

            # We ran off the end of the list
            if not current_node.next:
                raise KeyError('Value not found %s', val)

            current_node.next = current_node.next.next
            self.size -= 1

    def reverse(self) -> None:
        """Reverses the linked list.

        1. Set up previous, current, next
        2. Check head or next is not null
        3. while current exists:
            3.1 Set next node to be current.next
            3.2 Set current's next to be previous
            3.3 Set previous to be current
            3.4 Set current to be next
        4. Finally, set head to be previous

        Time: O(n)
        Space: O(1)

        :return: None
        """

        if not self._head or not self._head.next:
            return

        previous = None
        current = self._head
        next_node = None

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self._head = previous

    def is_empty(self) -> bool:
        return self.size == 0

    def __iter__(self):
        self.current = self._head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        val = self.current.val
        self.current = self.current.next
        return val
