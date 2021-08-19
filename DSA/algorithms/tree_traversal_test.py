import unittest

from algorithms.tree_traversal import inorder, preorder, postorder
from data_structures.binary_search_tree import BinarySearchTree


class TreeTraversalTest(unittest.TestCase):

    def test_inorder(self):
        bst = BinarySearchTree()
        bst.put(5, 5)
        bst.put(3, 3)
        bst.put(8, 8)
        bst.put(1, 1)
        bst.put(4, 4)
        bst.put(7, 7)
        bst.put(10, 10)
        nodes = []

        inorder(bst.root, nodes)

        self.assertListEqual([1, 3, 4, 5, 7, 8, 10], nodes)

    def test_preorder(self):
        bst = BinarySearchTree()
        bst.put(5, 5)
        bst.put(3, 3)
        bst.put(8, 8)
        bst.put(1, 1)
        bst.put(4, 4)
        bst.put(7, 7)
        bst.put(10, 10)
        nodes = []

        preorder(bst.root, nodes)

        self.assertListEqual([5, 3, 1, 4, 8, 7, 10], nodes)

    def test_postorder(self):
        bst = BinarySearchTree()
        bst.put(5, 5)
        bst.put(3, 3)
        bst.put(8, 8)
        bst.put(1, 1)
        bst.put(4, 4)
        bst.put(7, 7)
        bst.put(10, 10)
        nodes = []

        postorder(bst.root, nodes)

        self.assertListEqual([1, 4, 3, 7, 10, 8, 5], nodes)


if __name__ == '__main__':
    unittest.main()
