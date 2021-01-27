import unittest

from data_structures.ring_buffer import RingBuffer


class RingBufferTest(unittest.TestCase):

    def test_enqueue_dequeue(self):
        ring_buffer = RingBuffer(5)
        ring_buffer.enqueue(1)
        ring_buffer.enqueue(2)
        ring_buffer.enqueue(3)
        ring_buffer.enqueue(4)
        ring_buffer.enqueue(5)

        self.assertEquals(1, ring_buffer.dequeue())
        self.assertEquals(2, ring_buffer.dequeue())
        self.assertEquals(3, ring_buffer.dequeue())
        self.assertEquals(4, ring_buffer.dequeue())
        self.assertEquals(5, ring_buffer.dequeue())

    def test_circular_enqueue(self):
        ring_buffer = RingBuffer(3)
        ring_buffer.enqueue(1)
        ring_buffer.enqueue(2)
        ring_buffer.enqueue(3)

        self.assertEquals(1, ring_buffer.dequeue())

        ring_buffer.enqueue(4)
        self.assertEquals(2, ring_buffer.dequeue())
        self.assertEquals(3, ring_buffer.dequeue())
        self.assertEquals(4, ring_buffer.dequeue())

    def testInitWithInvalidCapacityRaisesValueError(self):
        with self.assertRaises(ValueError):
            RingBuffer(0)
