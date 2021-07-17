from typing import List, Any


def heap_sort(items: List[Any]) -> None:
    """A heap sort implementation.

    Remember: A (max) binary heap is an array where:
        * The max is at the root
        * The first child is given by 2i+1
        * The second child is given by  2i+2
        * The parent is given by (i-1)//2
        * Children are always larger than the parent

    1. First, we convert the array into array into a max binary heap using "heapify"
       This means the max element is at the root.

    2. Then, from the end of the heap (array), we:
        * Swap the last element with the root (max)
        * This means max element is at the end -- in it's correct place
        * Heapify to get the new root into it's correct place
            (max will now be at root again)
        * Decrement the end of heap (since max is in correct place)
            and repeat.

    The heapify process works as follows:

    Time: O(n log n)
    Space: O(1) -- in place.
    NOT stable.

    In practice, tends to be slower than quicksort.
    (Inner loop slower, lack of caching.)
    """
    _build_heap(items)

    end_of_heap_index = len(items) - 1

    while end_of_heap_index >= 0:
        _swap(items, 0, end_of_heap_index)
        # Heapify the root element to get
        # the smallest element at the root again
        _heapify(items, 0, end_of_heap_index)

        end_of_heap_index -= 1


def _build_heap(items: List[Any]) -> None:
    """Turns a list into a max heap.

    * Starting at the first non-root node (len // 2)-1...
    * While the node_index >= 0...
    * Heapify
    * Decrement node_index

    :param items: The items to sort.
    """
    # First non-leaf none will be n/2-1
    node_index = (len(items) // 2) - 1

    while node_index >= 0:
        _heapify(items, node_index, len(items))
        node_index -= 1


def _heapify(items: List[Any], node_index: int, end_of_heap: int) -> None:
    """Turns list from node_index to end_of_heap into a max heap.

     1. Get the left and right child indices
     2. If left child is larger, set that larger
     3. If right child is larger, set that larger
     4. If one of the child is larger, swap the values
        and.. Call heapify again with the new index.
     """
    largest = node_index
    left_child_index = (2 * node_index) + 1
    right_child_index = (2 * node_index) + 2

    # Work out if the left child or right child is larger than parent
    if left_child_index < end_of_heap and items[largest] < items[left_child_index]:
        largest = left_child_index

    if right_child_index < end_of_heap and items[largest] < items[right_child_index]:
        largest = right_child_index

    # if the parent isn't the largest index, swap and rerun
    # with new parent
    if largest != node_index:
        _swap(items, node_index, largest)
        # Here we call it "largest", but it's actually
        # the "old parent" -- it was swapped into a new
        # position (the old largest index)
        _heapify(items, largest, end_of_heap)


def _swap(items: List[Any], index_one, index_two) -> None:
    """Swaps 2 elements in a list."""
    items[index_one], items[index_two] = items[index_two], items[index_one]
