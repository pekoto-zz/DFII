import unittest

from algorithms.top_k_frequent import top_k_frequent_bucket_sort, top_k_frequent_pq


class TopKFrequentTest(unittest.TestCase):

    def test_top_k_frequent_bucket_sort(self):
        nums = [1, 1, 1, 2, 2, 2, 7, 4]
        k = 2

        top_k = top_k_frequent_bucket_sort(nums, k)

        self.assertListEqual([1, 2], top_k)

    def test_top_k_frequent_pq(self):
        nums = [1, 1, 1, 2, 2, 2, 7, 4]
        k = 2

        top_k = top_k_frequent_pq(nums, k)

        self.assertListEqual([1, 2], top_k)


if __name__ == '__main__':
    unittest.main()
