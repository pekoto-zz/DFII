import unittest

from data_structures.doubly_linked_list import DoublyLinkedList


class DoublyLinkedListTest(unittest.TestCase):

    def test_add_to_tail(self):
        deque = DoublyLinkedList()

        deque.add_to_tail(1)
        deque.add_to_tail(2)
        deque.add_to_tail(3)

        self.assertEqual(3, deque.size)
        self.assertEqual(1, deque._head.val)
        self.assertEqual(2, deque._head.next.val)
        self.assertEqual(3, deque._tail.val)

    def test_add_to_head(self):
        deque = DoublyLinkedList()

        deque.add_to_head(1)
        deque.add_to_head(2)
        deque.add_to_head(3)

        self.assertEqual(3, deque.size)
        self.assertEqual(3, deque._head.val)
        self.assertEqual(2, deque._head.next.val)
        self.assertEqual(1, deque._tail.val)

    def test_pop_head(self):
        deque = DoublyLinkedList()

        deque.add_to_tail(1)
        deque.add_to_tail(2)
        deque.add_to_tail(3)

        self.assertEqual(1, deque.pop_head())
        self.assertEqual(2, deque.size)
        self.assertEqual(2, deque.pop_head())
        self.assertEqual(1, deque.size)
        self.assertEqual(3, deque.pop_head())
        self.assertEqual(0, deque.size)

    def test_pop_tail(self):
        deque = DoublyLinkedList()

        deque.add_to_tail(1)
        deque.add_to_tail(2)
        deque.add_to_tail(3)

        self.assertEqual(3, deque.pop_tail())
        self.assertEqual(2, deque.size)
        self.assertEqual(2, deque.pop_tail())
        self.assertEqual(1, deque.size)
        self.assertEqual(1, deque.pop_tail())
        self.assertEqual(0, deque.size)

    def test_remove_val(self):
        deque = DoublyLinkedList()

        deque.add_to_tail(1)
        deque.add_to_tail(2)
        deque.add_to_tail(3)
        deque.add_to_tail(4)
        deque.add_to_tail(5)

        # Remove middle
        deque.remove_val(2)
        self.assertEqual(4, deque.size)
        self.assertEqual(3, deque._head.next.val)

        # Remove head
        deque.remove_val(1)
        self.assertEqual(3, deque.size)
        self.assertEqual(3, deque._head.val)

        # Remove tail
        deque.remove_val(5)
        self.assertEqual(2, deque.size)
        self.assertEqual(4, deque._tail.val)

        # Try removing non-existant value
        with self.assertRaises(KeyError):
            deque.remove_val(10)

    def test_reverse(self):
        deque = DoublyLinkedList()

        deque.add_to_tail(1)
        deque.add_to_tail(2)
        deque.add_to_tail(3)
        deque.add_to_tail(4)
        deque.add_to_tail(5)

        deque.reverse()

        self.assertEqual(5, deque._head.val)
        self.assertEqual(4, deque._head.next.val)
        self.assertEqual(3, deque._head.next.next.val)
        self.assertEqual(2, deque._head.next.next.next.val)
        self.assertEqual(1, deque._tail.val)
