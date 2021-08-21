import heapq
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


def top_k_frequent_pq(nums: List[int], k: int) -> List[int]:
    """Given a list of numbers, return the the top k most frequent numbers.

    Solved using priority queue approach.

    Example:
        nums: [1, 1, 1, 2, 2, 3], k=2
        output: [1, 2]

    1. Get the counts of each items, and turn them into tuples.
    2. Put the counts on a heap, popping the min off if the heap is > k
    3. Now we have a heap of size k with the largest elements

    (Note: We ensure k < n by checking at the start to get the
            times below.)

    Time: O(n log k): Where n is len(nums)
    Space: O(n+k): Where n is len(nums)
        n for the counts, and k for the heap
    """
    if k == len(nums):
        return nums

    # Build a hashmap of frequencies O(n)
    counts = Counter(nums)

    # Build the heap of size k O(n log k)
    heap = []
    for num, frequency in counts.items():   # O(n)
        heapq.heappush(heap, (frequency, num))  # O(k)
        if len(heap) > k:
            heapq.heappop(heap)

    # Get the elements in the heap O(k)
    return [element[1] for element in heap]



