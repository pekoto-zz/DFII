from collections import Counter
from typing import List


def top_k_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    """Given a list of numbers, return the the top k most frequent numbers.

    Solved using buckets sort approach.

    Example:
        nums: [1, 1, 1, 2, 2, 3], k=2
        output: [1, 2]

    1. Create a list of buckets to store frequencies.
        Note: no item can appear more than the length of the array
    2. Append each item to the frequency bucket.
        Ex. [[], [3], [2], [1], [], [], []]
    3. Flatten the list and return last k elements:
        [3, 2, 1]

    Time: O(n): Where n is len(nums)
    Space: O(n): Where n is len(nums) -- worst case, where every number unique.
    """
    # All items unique.
    if k == len(nums):
        return nums

    # Declare buckets for each frequency
    frequency_buckets = [[] for _ in range(len(nums) + 1)]

    # Gets count of item frequency
    counts = Counter(nums)

    # Add the numbers to the frequency buckets
    for num, frequency in counts.items():
        frequency_buckets[frequency].append(num)

    # Flatten the list
    flat_list = [item for sublist in frequency_buckets for item in sublist]

    # Return last k items in the list
    return flat_list[-k:]
