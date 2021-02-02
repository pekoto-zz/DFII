import sys
from typing import Any


class Node:
    """A node in a binary search tree.

    Has a:
        * Key
        * Value
        * Count (number of nodes below this node)
        * Left subtree
        * Right subtree
    """
    def __init__(self, key: Any, val: Any, count: int) -> None:
        """Initializes the tree node."""
        self.key = key
        self.val = val
        self.count = count

        self.left = None
        self.right = None


class BinarySearchTree:
    """A binary search tree (BST) implementation.

    A tree with a symmetric order:
        - Every element in the left subtree is < parent.
        - Evert element in the right subtree is > parent.

    This means we can do binary searches, since we know which direction
    to go at each step (left or right) by comparing to the key.

    Operations will typically take O(log n) time, but can take O(n) time
    if the values are inserted with a natural ordering (the tree will
    end up like a linked list).

    Uses:
        - Find k elements < value
        - Quick lookup/insert (if elements randomly ordered)
        - Print out min > max values (via inorder traversal)

    Operations:
        - put(key, val)
        - get(key)
        - remove(key)
        - size()
        - max()
        - min()
        - less_than(val)
        - ..._traversal() -- TODO
    """
    def __init__(self) -> None:
        """Initializes the BST."""
        self._root = None

    def put(self, key: Any, val: Any) -> None:
        """Puts a key/value into the key.

        Recursively add a node to the tree.

        1. If the node is empty, add it to the tree.
        2. If the node is < key, put it in the left subtree.
        3. If the node is > key, put it in the right subtree.
        4. If the node is == key, just update the value.
        5. Update the count: (left subtree size) + 1 + (right subtree size).
        6. Return the node.

                   2
                 /  \
                1    3
        > Insert 0
                   2
                 /  \
                1    3
               /
              0

        Time: O(log n), if elements random, O(n) worst case.

        :param key: The key to add.
        :param val: The value to associate with this key.
        :return: None.
        """
        self._root = self._put(self._root, key, val)

    def _put(self, node: Node, key: Any, val: Any) -> Node:
        """Put helper method."""
        if not node:
            return Node(key, val, 1)

        if key < node.key:
            # Add node to left subtree
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            # Add node to right subtree
            node.right = self._put(node.right, key, val)
        else:
            # Update the value of the existing node
            node.val = val

        # Set the count to be count in subtrees + 1
        node.count = self._size(node.left) + 1 + self._size(node.right)

        return node

    def get(self, key: Any) -> Any:
        """Returns the value for a given key.

        1. Set the node to head
        2. While it's not null...
            2.1 If the node.key == key, return value
            2.2 If the node.key < key, set node to be left node
            2.3 If the node.key > key, set node to be right node

        Time: O(log n) avg, O(n) worst case

        :param key: The key to find.
        :return: The value associated with that key.
        """
        node = self._root

        while node:
            if node.key == key:
                return node.val
            elif key < node.key:
                node = node.left
            else:
                node = node.right

        raise KeyError("Key not found!")

    def remove(self, key: Any) -> None:
        """Removes a node from the binary search tree.

        This is probably the most complex operation, as we need to
        to ensure the BST remains valid when removing a node.

        1. If the key is smaller, we remove in the left subtree.
        2. If the key is larger, we remove in the right subtree.
        3. Once we find the node to remove, things get tricky...

           3.1 If the node has no right subtree, set the node to be the left subtree,
               and vice-versa.
           Remove "1" (replaces with 1.5):
              2
             / \
            1   3
            \
             1.5
          (No left subtree, so right subtree must be next smallest)

        3.2 If the node has left and right subtrees, replace the node with the smallest
            value in the right subtree.

            Remove "7" (replaces with 6.5)
            10
           / \
          7    12
         / \
        2   8
           /
          6
           \
           6.5

        Time:
            Average: O(n)
            Worst: O(sqrt(n))

        :param key: The value to remove.
        :return: None.
        """
        self._root = self._remove(self._root, key)

    def _remove(self, node: Node, key: Any) -> Node:
        """Recursive helper function."""
        if not node:
            raise KeyError("Key not found!")

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Node has left and right subtrees.
            node_to_delete = node

            # Replace the node with the smallest node in the right subtree
            node = _min(node_to_delete.right)

            # Set right to be the right subtree with the smallest node removed
            node.right = self._delete_min(node_to_delete.right)

            # Set left to the left subtree
            node.left = node_to_delete.left

        node.count = _size(node.left) + 1 + _size(node.right)

    def _delete_min(self, node: Node) -> Node:
        """Deletes the minimum node in a subtree.

        Once we hit a leftmost node, the min node will be that tree's right node.

        1. If the node in the left is null, return node.right.
        2. Delete from the left subtree.
        3. Update the count.

          7
         / \
        2   8
           /
          6
           \
           6.5


        :param node: The node to delete the min from.
        :return: The subtree with the minimum node deleted.
        """
        if not node.left:
            return node.right

        node.left = self._delete_min(node.left)
        node.count = self._size(node.left) + 1 + self._size(node.right)
        return node

    def size(self) -> int:
        """Returns the size of the tree."""
        return self._size(self._root)

    def is_valid(self) -> bool:
        """Checks that the BST is valid.
        (Assuming the tree is made of integers)

        Pass in a min and max bound.
        The node on the left must be between the min bound and less than the node's key.
        The node on the right must be greater than the node's key and less than the max bound.

        :return: True if the BST is valid.
        """
        return self._is_valid(self._root, sys.minsize, sys.maxsize)

    def _is_valid(self, node: Node, min_bound: int, max_bound: int) -> bool:
        """Recursive helper function."""
        if not node:
            return True

        if node.key < min_bound or node.key > max_bound:
            return False

        return (self._is_valid(node.left, min_bound, node.key)
                and self._is_valid(node.right, node.key, max_bound))


def _size(node: Node) -> int:
    return 0 if not node else node.count


def _min(node: Node) -> Node:
    """Gets the minimum node from the tree"""
    if not node:
        raise Exception("Tried to get min on empty tree.")

    while node.left:
        node = node.left

    return node
