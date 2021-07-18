from typing import List, Any


def quicksort(items: List[Any]) -> None:
    """A quicksort implementation.

    * While left < right
    * Partition the array.3
    * Recursively sort the left half.
    * Recursively sort the right half.

    Time: O(n log n) -- average
          O(n^2) -- worst, happens when pivot is max/min in sorted array
                    (i.e. array sorted). Can avoid by shuffling first.

    Space: log(n) -- recursive calls.

    NOT stable.

    :param items: The list of items to sort.
    """
    _quicksort(items, 0, len(items)-1)


def _quicksort(items: List[Any], left: int, right: int) -> None:
    """Helper function.

    Partition the array:
        Partition is in the correct position.
        Sort the LHS.
        Sort the RHS.
    """
    if left < right:
        pivot_index = _partition(items, left, right)

        _quicksort(items, left, pivot_index-1)
        _quicksort(items, pivot_index+1, right)


def _partition(items: List[Any], left: int, right: int) -> int:
    """Partitions the array around the pivot value.

    Picks a pivot value and sorts everything to the left <= pivot,
    and everything greater than pivot to the right.

    At the end, the pivot will be in its correct position.

    Example: [100, 5, -2, 1, 52, 3, 4]

    1. Pick a pivot value.
    2. Set a pointer to the left -- this is the greatest element.
    3. Iterate until the pivot.
        3.1 If we find an element <= pivot
        3.2 Swap it with the greater value
        3.3 Increment greater element pivot
    4. Swap the pivot with the greater element pointer
    5. Return the pivot position.

    Args:
        items: The list of items to sort.
        left: The leftmost index.
        right: The rightmost index.

    Returns: The index of the pivot value.
    """
    # Choose rightmost element as pivot.
    pivot_val = items[right]

    # Greater element pointer
    # We know the pointer must point to something greater
    # because if not it would have been swapped.
    i = left

    for j in range(left, right):
        if items[j] <= pivot_val:
            # An item smaller than the pivot was found:
            # Swap it with the greater element (i)
            items[i], items[j] = items[j], items[i]
            i += 1

    # Swap the pivot element with the greater element
    items[i], items[right] = items[right], items[i]

    # Return position where partition finished
    return i
