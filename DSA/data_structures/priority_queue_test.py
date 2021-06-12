import unittest

from data_structures.priority_queue import PriorityQueue


class PriorityQueueTest(unittest.TestCase):

    def test_add(self):
        priority_queue = PriorityQueue(5)

        priority_queue.add(1)
        priority_queue.add(2)
        priority_queue.add(3)
        priority_queue.add(4)
        priority_queue.add(5)
        priority_queue.add(6)
        priority_queue.add(7)
        priority_queue.add(8)
        priority_queue.add(9)
        priority_queue.add(10)

        self.assertEqual(10, priority_queue.size)

    def test_pop(self):
        priority_queue = PriorityQueue()

        priority_queue.add(1)
        priority_queue.add(2)
        priority_queue.add(3)
        priority_queue.add(4)
        priority_queue.add(5)
        priority_queue.add(6)
        priority_queue.add(7)
        priority_queue.add(8)
        priority_queue.add(9)
        priority_queue.add(10)

        self.assertEqual(10, priority_queue.pop())
        self.assertEqual(9, priority_queue.pop())
        self.assertEqual(8, priority_queue.pop())
        self.assertEqual(7, priority_queue.pop())
        self.assertEqual(6, priority_queue.pop())
        self.assertEqual(5, priority_queue.pop())
        self.assertEqual(4, priority_queue.pop())
        self.assertEqual(3, priority_queue.pop())
        self.assertEqual(2, priority_queue.pop())
        self.assertEqual(1, priority_queue.pop())

    def test_pop_empty_queue_raises_exception(self):
        priority_queue = PriorityQueue()

        with self.assertRaises(Exception):
            priority_queue.pop()


if __name__ == '__main__':
    unittest.main()
