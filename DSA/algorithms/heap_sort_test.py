import unittest

from algorithms.heap_sort import heap_sort


class HeapSortTest(unittest.TestCase):

    def test_heap_sort(self):
        arr = [50, 1, -4, 3, 20, 200, 9]

        heap_sort(arr)

        self.assertListEqual([-4, 1, 3, 9, 20, 50, 200], arr)


if __name__ == '__main__':
    unittest.main()
