import unittest

from data_structures.linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def testAddRecursive(self):
        linked_list = LinkedList()
        linked_list.add_recursive(1)
        linked_list.add_recursive(2)
        linked_list.add_recursive(3)

        self.assertEqual(3, linked_list.size)
        self.assertEqual(1, linked_list._head.val)
        self.assertEqual(2, linked_list._head.next.val)
        self.assertEqual(3, linked_list._head.next.next.val)

    def testAddIterative(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)

        self.assertEqual(3, linked_list.size)
        self.assertEqual(1, linked_list._head.val)
        self.assertEqual(2, linked_list._head.next.val)
        self.assertEqual(3, linked_list._head.next.next.val)

    def testIsEmpty(self):
        linked_list = LinkedList()
        self.assertTrue(linked_list.is_empty())
        linked_list.add_recursive(1)
        self.assertFalse(linked_list.is_empty())

    def testRemoveRecursive(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)

        linked_list.remove_recursive(1)
        self.assertEqual(2, linked_list._head.val)
        self.assertEqual(3, linked_list._head.next.val)
        self.assertEqual(2, linked_list.size)

        linked_list.remove_recursive(3)
        self.assertEqual(2, linked_list._head.val)

        linked_list.remove_recursive(2)
        self.assertTrue(linked_list.is_empty())

    def testRemoveIterative(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)
        linked_list.add_iterative(4)
        linked_list.add_iterative(5)

        # Remove the head
        linked_list.remove_iterative(1)
        self.assertEqual(2, linked_list._head.val)
        self.assertEqual(3, linked_list._head.next.val)
        self.assertEqual(4, linked_list._head.next.next.val)
        self.assertEqual(5, linked_list._head.next.next.next.val)
        self.assertEqual(4, linked_list.size)

        # Remove the tail
        linked_list.remove_iterative(5)
        self.assertEqual(2, linked_list._head.val)
        self.assertEqual(3, linked_list._head.next.val)
        self.assertEqual(4, linked_list._head.next.next.val)
        self.assertEqual(3, linked_list.size)

        # Remove element in the middle
        linked_list.remove_iterative(3)
        self.assertEqual(2, linked_list._head.val)
        self.assertEqual(4, linked_list._head.next.val)
        self.assertEqual(2, linked_list.size)

        # Remove element not found
        with self.assertRaises(KeyError):
            linked_list.remove_iterative(5)

    def testIteration(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)
        linked_list.add_iterative(4)
        linked_list.add_iterative(5)

        for node in linked_list:
            print(f'Node is: {node}')

        self.assertTrue(True)

    def testReverse(self):
        linked_list = LinkedList()
        linked_list.add_iterative(1)
        linked_list.add_iterative(2)
        linked_list.add_iterative(3)
        linked_list.add_iterative(4)
        linked_list.add_iterative(5)

        linked_list.reverse()

        self.assertEqual(5, linked_list._head.val)
        self.assertEqual(4, linked_list._head.next.val)
        self.assertEqual(3, linked_list._head.next.next.val)
        self.assertEqual(2, linked_list._head.next.next.next.val)
        self.assertEqual(1, linked_list._head.next.next.next.next.val)
        self.assertEqual(5, linked_list.size)