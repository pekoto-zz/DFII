from typing import List, Any


def insertion_sort(items: List[Any]) -> None:
    """Insertion sort implementation.

    Insertion sort is good if the array is already sorted.

    Best case: O(n) -- already sorted.
    Worst case: O(n^2) -- reverse sorted.

    Stable.
    Space: O(1)

    1. Iterate around the array.
    2. If the element is smaller than the previous element,
        then swap the elements.
    """
    for i in range(1, len(items)):
        j = i

        while j > 0 and items[j] < items[j-1]:
            # While element is smaller than the one before it,
            # swap the elements.
            items[j-1], items[j] = items[j], items[j-1]
            j -= 1
