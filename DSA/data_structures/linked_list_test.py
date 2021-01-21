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

