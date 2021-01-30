import unittest

from data_structures.array_queue import ArrayQueue


class ArrayQueueTest(unittest.TestCase):

    def test_enqueue(self):
        array_queue = ArrayQueue()
        array_queue.enqueue(1)
        array_queue.enqueue(2)
        array_queue.enqueue(3)

        self.assertEquals(3, array_queue.size)

    def test_dequeue(self):
        array_queue = ArrayQueue()
        array_queue.enqueue(1)
        array_queue.enqueue(2)
        array_queue.enqueue(3)

        self.assertEquals(1, array_queue.dequeue())
        self.assertEquals(2, array_queue.dequeue())
        self.assertEquals(3, array_queue.dequeue())

        self.assertEquals(0, array_queue.size)

        array_queue.enqueue(4)
        array_queue.enqueue(5)

        self.assertEquals(4, array_queue.dequeue())
        self.assertEquals(1, array_queue.size)

    def test_grow(self):
        array_queue = ArrayQueue(2)
        array_queue.enqueue(1)
        array_queue.enqueue(2)
        array_queue.enqueue(3)
        array_queue.enqueue(4)
        array_queue.enqueue(5)

        self.assertEquals(5, array_queue.size)

        self.assertEquals(1, array_queue.dequeue())
        self.assertEquals(2, array_queue.dequeue())
        self.assertEquals(3, array_queue.dequeue())
        self.assertEquals(4, array_queue.dequeue())
        self.assertEquals(5, array_queue.dequeue())

        self.assertEquals(0, array_queue.size)

    def test_init_with_invalid_capacity_raises_value_error(self):
        with self.assertRaises(ValueError):
            ArrayQueue(0)









