from typing import List, Any


def mergesort(items: List[Any]) -> List[Any]:
    """A merge sort implementation.

    Time: O(n log n)
    Space: O(n) -- for auxiliary arrays.

    STABLE: Yes.

    Use for sorting linked lists.
    Use if all the data can't fit into memory
        (Sort into temporary files/storage,
         combine sorted files/temporary storage.)

    * if len <= 1, return
    * Get mid
    * Mergesort the two halves recursively (n sublists)
    * Merge the two halves.

    :param items: The list of items to sort.
    :return: The sorted list of items.
    """

    # Base case: 1-element array must be sorted.
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left_partition = mergesort(items[:mid])
    right_partition = mergesort(items[mid:])

    return _merge(left_partition, right_partition)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    """Merges two arrays into one.

    * Set up 2 pointers for both arrays.
    * Take the lowest element from both arrays and copy it into the merged output.
    * Copy the remaining elements from either array.

    :param left: The left array partition.
    :param right: The right array partition.
    :return: Left and right partitions merged into one array.
    """
    i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
