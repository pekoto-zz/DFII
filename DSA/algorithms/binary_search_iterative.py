from typing import List


def binary_search(arr: List[int], key: int) -> int:
    """Returns the index of a given key in a sorted array, or -1 if key not found.

    1. Get left and right indices.
    2. Calculate the mid.
    3. Depending on whether the key is bigger or smaller than mid,
       update left of right.

    Space: O(1)
    Time: log(n)

    :param arr: The sorted array to search
    :param key: The key to search for
    :return: The index of the key if found, -1 otherwise
    """
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = left + (right-left)//2

        if key > arr[mid]:
            left = mid+1
        elif key < arr[mid]:
            right = mid-1
        else:
            return mid

    # Key not found
    return -1
