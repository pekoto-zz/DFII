import unittest

from data_structures.binary_search_tree import BinarySearchTree


class BinarySearchTreeTest(unittest.TestCase):

    def test_put(self):
        bst = BinarySearchTree()
        bst.put("1", 1)
        bst.put("2", 2)
        bst.put("3", 3)

        self.assertEqual(3, bst.size())

    def test_get(self):
        """Warning: Python will lexicographically sort numerical strings lol.
        (I.e., "5" is less than "10".)
        """
        bst = BinarySearchTree()
        bst.put("1", 1)
        bst.put("2", 2)
        bst.put("3", 3)

        self.assertEqual(1, bst.get("1"))
        self.assertEqual(2, bst.get("2"))
        self.assertEqual(3, bst.get("3"))

        with self.assertRaises(KeyError):
            bst.get("4")

    def test_remove(self):
        bst = BinarySearchTree()
        bst.put(10, "10")
        bst.put(5, "5")
        bst.put(1, "1")
        bst.put(20, "20")
        bst.put(50, "50")
        bst.put(7, "7")

        bst.remove(10)  # Removes root
        bst.remove(50)  # Removes max node
        bst.remove(1)   # Removes min node

        with self.assertRaises(KeyError):
            bst.get(10)

        with self.assertRaises(KeyError):
            bst.get(50)

        with self.assertRaises(KeyError):
            bst.get(1)

        self.assertEqual("5", bst.get(5))
        self.assertEqual("20", bst.get(20))
        self.assertEqual("7", bst.get(7))

    def test_is_valid(self):
        bst = BinarySearchTree()
        bst.put(10, "10")
        bst.put(5, "5")
        bst.put(1, "1")
        bst.put(20, "20")
        bst.put(50, "50")
        bst.put(7, "7")

        self.assertTrue(bst.is_valid())


if __name__ == '__main__':
    unittest.main()
