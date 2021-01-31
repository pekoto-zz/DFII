import unittest

from data_structures.lru_cache import LruCache


class LruCacheTest(unittest.TestCase):

    def test_add(self):
        lru_cache = LruCache()
        lru_cache.add("1", 1)
        lru_cache.add("2", 2)
        lru_cache.add("3", 3)

        self.assertEquals(3, lru_cache.size)
        self.assertEquals(1, lru_cache._least_recently_used.next.val)
        self.assertEquals(3, lru_cache._most_recently_used.previous.val)

    def test_add_update_value(self):
        lru_cache = LruCache()
        lru_cache.add("1", 1)
        lru_cache.add("2", 2)
        lru_cache.add("3", 3)
        lru_cache.add("2", "two")

        self.assertEquals(3, lru_cache.size)
        self.assertEquals(1, lru_cache._least_recently_used.next.val)
        self.assertEquals("two", lru_cache._most_recently_used.previous.val)

    def test_get(self):
        lru_cache = LruCache()
        lru_cache.add("1", 1)
        lru_cache.add("2", 2)
        lru_cache.add("3", 3)

        self.assertEquals(3, lru_cache.size)

        self.assertEquals(3, lru_cache.get("3"))
        self.assertEquals(2, lru_cache.get("2"))
        self.assertEquals(1, lru_cache.get("1"))

        self.assertEquals(3, lru_cache._least_recently_used.next.val)
        self.assertEquals(1, lru_cache._most_recently_used.previous.val)

    def test_add_over_capacity_removes_least_recently_used(self):
        lru_cache = LruCache(2)
        lru_cache.add("1", 1)
        lru_cache.add("2", 2)
        lru_cache.add("3", 3)  # Removes LRU value

        self.assertEquals(2, lru_cache.size)

        with self.assertRaises(KeyError):
            lru_cache.get("1")


if __name__ == '__main__':
    unittest.main()
