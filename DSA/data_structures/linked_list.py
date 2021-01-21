from typing import Any


class Node:

    def __init__(self, val: Any=None) -> None:
        self.val = val
        self.next = None

    def __str__(self):
        return self.val


class LinkedList:

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

    def is_empty(self) -> bool:
        return self.size == 0
