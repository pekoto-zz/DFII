import unittest

from data_structures.trie import Trie


class TrieTest(unittest.TestCase):

    def test_get(self):
        trie = Trie()

        trie.add("Dog", "Dog")
        trie.add("Cat", "Cat")
        trie.add("Caterpillar", "Caterpillar")
        trie.add("Doge", "Doge")

        self.assertEqual("Dog", trie.get("Dog"))
        self.assertEqual("Cat", trie.get("Cat"))
        self.assertEqual("Caterpillar", trie.get("Caterpillar"))
        self.assertEqual("Doge", trie.get("Doge"))

    def test_keys(self):
        trie = Trie()

        trie.add("Dog", "Dog")
        trie.add("Cat", "Cat")
        trie.add("Doge", "Doge")

        expected_keys = ["Cat", "Dog", "Doge"]

        self.assertEqual(expected_keys, trie.keys())

    def test_keys_with_prefix(self):
        trie = Trie()

        trie.add("Dog", "Dog")
        trie.add("Cat", "Cat")
        trie.add("Doge", "Doge")

        self.assertEqual(["Dog", "Doge"], trie.keys_with_prefix("Dog"))

        with self.assertRaises(KeyError):
            trie.keys_with_prefix("Zebra")

    def test_longest_prefix(self):
        trie = Trie()

        trie.add("Dog", "Dog")
        trie.add("Cat", "Cat")
        trie.add("Doge", "Doge")

        self.assertEqual("Doge", trie.longest_prefix("Dogele"))


if __name__ == '__main__':
    unittest.main()
