from typing import Any


class Stack:
    """A LIFO queue. Can also be implemented using a linked list.

    Operations:
    Push: O(1) [O(n) amortized if implemented using an array]
    Peek/Pop: O(1) [O(n) amortized if implemented using an array]

    Uses:
        * Browser back button
        * Undo function
        * Interpreter:
            * pop values on value stack
            * pop operators on operator stack
            * At right parenthesis, pop operator and two values
            * Put the value back on the stack
    """

    def __init__(self):
        self._stack = []
        self.size = 0

    def push(self, val: Any) -> None:
        """Pushes a value onto the stack.

        :param val: The value to add to the stack.
        :return: None.
        """
        self._stack.append(val)
        self.size += 1

    def peek(self) -> Any:
        """Returns the value at the top of the stack.

        :return: The value at the top of the stack.
        """
        if self.size == 0:
            raise Exception('Stack is empty')

        return self._stack[-1]

    def pop(self) -> Any:
        """Removes and returns the value at the top of the stack.

        :return: The value at the top of the stack.
        """
        if self.size == 0:
            raise Exception('Stack is empty')

        val = self._stack.pop()
        self.size -= 1

        return val
