from typing import Any

_DEFAULT_CAPACITY = 10


class ArrayQueue:
    """A FIFO queue implemented using an array internally.

    The main issue here is that we will occasionally shrink
    or grow our queue capacity based on the current size.
    But in return we get on average O(1) operations.

    enqueue: O(1) average, O(n) amortized
    dequeue: O(1), O(n/2) amortized
    """

    def __init__(self, capacity=_DEFAULT_CAPACITY):
        self._start = 0
        self._end = 0
        self.size = 0

        if capacity < 1:
            raise ValueError('Capacity must be at least 1')

        self._queue = [None] * capacity

    def enqueue(self, val: Any) -> None:
        """Adds an item to the end of the queue.

        1. If we reached capacity (end = len), double the size
        2. Add a value to the end of the queue
        3. Increment end pointer and size.

        Time: O(1) average, O(n) amortized.

        :param val: The value to add.
        :return: None.
        """
        if self._end == len(self._queue):
            self._grow(len(self._queue) * 2)

        self._queue[self._end] = val  # We can't use append because that will always add to the end.
        self._end += 1
        self.size += 1

    def _grow(self, new_size: int) -> None:
        """Extend the queue to a new size."""
        self._queue.extend([None] * new_size)

    def dequeue(self) -> Any:
        """Removes and returns the item from the front of the queue.

        1. If the queue is empty, raise an exception.
        2. Get the value from the start.
        3. Set the start to none.
        4. Increment start pointer.
        5. If start == end, reset both to 0 (queue empty).
        6. If the end is 1/4 of queue size, shrink the queue by half.

        Time: O(1) average, O(n/2) amortized.

        :return: The front of the queue.
        """
        if self.is_empty():
            raise Exception('Queue is empty.')

        val = self._queue[self._start]
        self._queue[self._start] = None
        self._start += 1

        # We dequeued everything
        if self._start == self._end:
            self._start = 0
            self._end = 0

        if self._end == int(len(self._queue) / 4):
            self._shrink(int(len(self._queue) / 2))

        self.size -= 1

        return val

    def _shrink(self, new_size: int) -> None:
        """Shrinks the queue to a new size."""
        self._queue = self._queue[:new_size + 1]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty."""
        return self.size == 0
