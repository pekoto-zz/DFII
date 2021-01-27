from typing import Any


class RingBuffer:
    """A circular FIFO queue that uses a fixed amount of space.

    This lets us efficiently queue and dequeue objects in O(1) time,
    and let us access objects in O(1) time without having to resize.
    The downside is that we CAN'T resize.

    * Enqueue: O(1)
    * Dequeue: O(1)
    """

    def __init__(self, capacity: int) -> None:
        """Initializes the buffer."""
        if capacity < 1:
            raise ValueError('Capacity must be at least 1.')

        self._used_space = 0
        self._write_pos = 0
        self._queue = [None] * capacity

    def enqueue(self, val: Any) -> bool:
        """Adds an item to the queue if space available.

        1. If the write position is >= len of array, set it back to 0 (circle back)
        2. Add the item and increment write position and used space.

        Time: O(1)

        :param val: The item to add to the queue.
        :return: True if the item could be added, False otherwise (queue full).
        """
        if self._used_space == len(self._queue):
            return False

        if self._write_pos >= len(self._queue):
            self._write_pos = 0

        self._queue[self._write_pos] = val
        self._write_pos += 1
        self._used_space += 1

        return True

    def dequeue(self) -> Any:
        """Returns the front of the queue.

        This involves some calculations to "circle" around the ring.

        1. Get the read pos by write_pos-used_space
        2. If it's less than 0, add the len of the queue
        3. Get the value, set it to None, and return the value

        Time: O(1)

        :return: The item that was least-recently added to the queue.
        """
        if self._used_space == 0:
            raise Exception('Queue is empty.')

        read_pos = self._write_pos - self._used_space

        if read_pos < 0:
            # Buffer has wrapped around
            read_pos += len(self._queue)

        val = self._queue[read_pos]
        self._queue[read_pos] = None
        self._used_space -= 1

        return val
