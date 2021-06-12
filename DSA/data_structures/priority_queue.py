from typing import Any

_DEFAULT_SIZE = 10
_TOP_OF_HEAP_INDEX = 1


class PriorityQueue:
    """A priority queue (binary heap) implementation.

    This is a complete (perfectly balanced except for trailing nodes) binary tree
    implementation (each parent has at most 2 children).

    Specifically this is a max heap, where the node with the max value is at the top of the heap.

    Parent node = node_index / 2
    Child node one = node_index * 2
    Child node two = node_index * 2 + 1

    The difference between this and a tree is that the tree is for searching,
    and this is just for getting the next max.

    Time:
        Add: O(log n)
        Remove max/min: O(log n)

    Interface:
        add: Adds a node at the end of the tree and SWIMs it up.
                (Swim: keep swapping child with parent while parent is bigger and past top of the heap.)

        remove_max: Swaps the top (min/max) node with the last node, removes it, and then
                    SINKs the new top node down.
                    (Sink: keep swapping parent node with LARGER child node while parent node is smaller
                           and not past the bottom of the heap.)

    Gotcha: Start indexing at 1 to make the maths easier.
    """
    def __init__(self, size: int = _DEFAULT_SIZE) -> None:
        """Initializes the priority queue.

        :param size: The initial size for the queue.
        """
        self._heap = [None] * size
        self._end_of_heap_index = 1
        self.size = 0

    def add(self, val: Any) -> None:
        """Adds a value to the heap.

        1. Check for resize.
        2. Add the new value to the bottom of the heap.
        3. Swim the element to the correct position.
        4. Increment next element pointer (new bottom).

        Time: O(log n)

        :param val: The value to add.
        :return: None.
        """
        if self._end_of_heap_index == len(self._heap):
            self._grow(len(self._heap))

        self._heap[self._end_of_heap_index] = val
        self._swim(self._end_of_heap_index)
        self._end_of_heap_index += 1
        self.size += 1

    def _grow(self, new_size: int) -> None:
        """Extend the queue to a new size."""
        self._heap.extend([None] * new_size)

    def _swim(self, child_index: int) -> None:
        """Swims the child up to the top of the heap while it is larger than its parent.

        1. While not past the top of the heap...
        2. ...And while the child is bigger than its parent.
        3. Swap the child with its parent.

        :param child_index: The newly added node index to swim up.
        :return: None.
        """
        parent_index = int(child_index / 2)

        while child_index > _TOP_OF_HEAP_INDEX and self._less_than(parent_index, child_index):
            self._swap(parent_index, child_index)
            child_index = parent_index
            parent_index = int(parent_index/2)

    def _less_than(self, index_one: int, index_two: int) -> bool:
        """Returns True if element at index_one is less than the element at index_two.

        :param index_one: The first element to compare.
        :param index_two: The second element to compare.
        :return: True if element at index_one is less than the element at index_two.
        """
        return self._heap[index_one] < self._heap[index_two]

    def _swap(self, index_one: int, index_two: int) -> None:
        """Swaps two elements in the heap.

        :param index_one: The first element index.
        :param index_two: The second element index.
        :return: None.
        """
        temp = self._heap[index_one]
        self._heap[index_one] = self._heap[index_two]
        self._heap[index_two] = temp

    def pop(self) -> Any:
        """Returns the max value in the heap.

        1. Decrement the end of heap pointer.
        2. Swap the largest (top) node with the end of heap.
        3. Save largest value for return.
        4. Get rid of the reference to the largest value.
        5. Sink the new top to its correct position.
        6. Check for resize.
        7. Return the max value.

        :return: The max value in the heap.
        """
        if self.size == 0:
            raise Exception("Cannot pop empty heap.")

        self._end_of_heap_index -= 1
        self._swap(_TOP_OF_HEAP_INDEX, self._end_of_heap_index)

        # Removes the top value for return.
        # (Cannot use .pop as this will shrink the heap.)
        val = self._heap[self._end_of_heap_index]
        self._heap[self._end_of_heap_index] = None

        self._sink(_TOP_OF_HEAP_INDEX)

        if self._end_of_heap_index == len(self._heap) / 4:
            # Shrinks heap to free used space
            new_size = int(len(self._heap)/2)
            self._heap = self._heap[:new_size]

        self.size -= 1

        return val

    def _sink(self, parent_index: int) -> None:
        """Sinks a node down to its correct position.

        1. Get the child indices.
        2. While the node is not off the end of the heap and a child is greater than this node...
        3. Swap the node with the greatest child.

              6
            /  \
           5    8
        ->
              8
            /  \
           5    6

        :param parent_index: The index of the node to sink down.
        :return: None.
        """
        child_one_index = parent_index * 2
        child_two_index: int
        max_child_index: int

        while child_one_index < self._end_of_heap_index:
            # Check if we have a second child
            #  0 1 2 3 4 5 6 7
            # | | | |6| | |8| |
            # Parent = 3, end_of_heap = 6, child_one_index = 6, end_of_heap-2 = 4
            if child_one_index <= self._end_of_heap_index - 2:
                child_two_index = child_one_index + 1
                max_child_index = self._max(child_one_index, child_two_index)
            else:
                max_child_index = child_one_index

            if self._less_than(parent_index, max_child_index):
                self._swap(parent_index, max_child_index)
                parent_index = max_child_index
                child_one_index = parent_index*2
            else:
                break

    def _max(self, index_one: int, index_two: int) -> int:
        """Returns the index with a greater element in the heap.

        :param index_one: The first index to compare.
        :param index_two: The second index to compare.
        :return: The index with a greater value in the heap.
        """
        if self._less_than(index_one, index_two):
            return index_two
        else:
            return index_one
