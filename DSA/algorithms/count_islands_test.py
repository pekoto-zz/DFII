import unittest

from algorithms.count_islands import count_islands


class CountIslandsTest(unittest.TestCase):

    def test_count_islands(self):
        matrix = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
        expected_num_of_islands = 3

        actual_num_of_islands = count_islands(matrix)

        self.assertEqual(expected_num_of_islands, actual_num_of_islands)


if __name__ == '__main__':
    unittest.main()
