from typing import List


def counting_sort(items: List[int]) -> None:
    """A counting sort implementation.

    Can be good for counting some enums or something with
    a small radix.

    1. Set up a count array of size max_val+1.
    2. For each item in input, increment the count of that item.
    3. Get the cumulative counts for the count array.
    4. Now iterate around the input array: the sorted position is given by
        counts[input_elem]-1. Decrement the count by 1.
    5. Finally, copy the output array back to the main array.

    Performance: O(n+r) -- where r is radix size, and n is array size
                 n = loop over array
                 r = get counts
    Space: O(n + r)
    STABLE but not in-place.
    """

    # Sets up an array to hold counts for each element.
    max_val = max(items)+1
    counts = [0] * max_val

    # Sets up an auxiliary array to hold the output.
    output = [0] * len(items)

    # Store the count of each element
    # Example:
    # items  = [4, 4, 2, 1]
    # counts = [0, 1, 1, 0, 2]
    for item in items:
        counts[item] += 1

    # Store the cumulative counts of each element.
    # Example:
    # counts  = [0, 1, 1, 0, 2]
    # counts* = [0, 1, 2, 2, 4]
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # Copy to output. The correct position is given by count array val-1.
    # Example:
    # items = [4, 4, 2, 1]
    # counts = [0, 1, 1, 2, 3]
    # output = [.., .., .., 4] <- count[4-1] = count[3]
    for item in items:
        # Get the output index
        output_index = counts[item]-1
        output[output_index] = item
        counts[item] -= 1

    # Copy back to the original list
    for i, elem in enumerate(output):
        items[i] = elem
