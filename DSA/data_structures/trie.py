# Num of chars in extended ASCII
from typing import Any, List

_DEFAULT_RADIX_SIZE = 256


class Node:
    """Node class for use in the Trie.

    Each Node contains len(radix) children.
    """
    def __init__(self, radix_size: int) -> None:
        self.val = None
        self.children = [None] * radix_size


class Trie:
    """A basic R-way Trie ("try"). Each node contains len(radix) children (i.e., R children).

    A node represents a character in the radix, and has R-children,
    representing the next character in the sequence. Strings are inserted one character at a time.

    The termination of a string is marked by an inserted value.

    So when searching, we just move down the tree until:
     - We hit a null link (node children are all null).
     - The char we are looking for does not exist as a child.

    Performance:
        Put: O(n)
        Search: O(n) (though typically less than this for misses, since we terminate early.)
                Search performance can typically best a HashMap for strings.

        Memory:
            O(L*N*radix) -- number of strings * string length * radix size.
            This is a downside of a tree, though it can be compressed in various ways).

        Uses:
            - Quick string matching
            - Spell checker
            - Prefix matching
    """
    def __init__(self, radix_size: int=_DEFAULT_RADIX_SIZE) -> None:
        self._radix_size = radix_size
        self._root = None

    def add(self, key: str, val: Any) -> None:
        """Adds key/val to the trie.

        1. If the node doesn't exist, instantiate it.
        2. If the index we're at is the length of the key, set value and return.
        3. Else, get the ASCII value of the char at this index.
        4. Set the child at this position to be the next char in the key.
        5. Return the node.

        Time: O(n)
        """
        self._root = self._add(self._root, key, val, 0)

    def _add(self, node: Node, key: str, val: Any, key_index: int) -> Node:
        """Recursive helper function."""
        if not node:
            node = Node(self._radix_size)

        # We reached the end of our key.
        if key_index == len(key):
            node.val = val
            return node

        # Add the next char in the key to our trie.
        # Think of it like, stepping through our key string and
        # stepping down our trie at the same time.
        child_index = ord(key[key_index])
        node.children[child_index] = self._add(node.children[child_index], key, val, key_index + 1)

        return node

    def get(self, key: str) -> Any:
        """Returns the value from the trie, or raises KeyError if not found.

        1. If the node is null, throw a key error.
        2. If the str_index == the length of the key, we found it.
        3. Recurse with the next char in the key.
           (Step through key, and down trie.)

        Time: O(n), where n is the length of the string.
              Although mismatches will typically have better performance.
        """
        node = self._get(self._root, key, 0, )

        return node.val

    def _get(self, node: Node, key: str, key_index: int) -> Node:
        """Recursive helper function."""
        if not node:
            raise KeyError("Key not found!")

        if key_index == len(key):
            # Finished searching
            return node

        child_index = ord(key[key_index])

        return self._get(node.children[child_index], key, key_index + 1, )

    def keys(self) -> List[str]:
        """Gets every key in the trie.

        1. If node is null, return.
        2. If the node is a value, add this prefix.
        3. Otherwise, iterate around the radix and check every child.
           (next child index, and add this char to the prefix).

        Time: O(N*radix_size), where N is the number of strings.
        """
        keys = []
        self._traverse_tree(self._root, "", keys)
        return keys

    def _traverse_tree(self, node: Node, prefix: str, keys: List[str]) -> None:
        """Recursive helper function."""
        if not node:
            return

        if node.val:
            keys.append(prefix)

        for char_index in range(0, self._radix_size):
            self._traverse_tree(node.children[char_index], prefix + chr(char_index), keys)

    def keys_with_prefix(self, prefix: str) -> List[str]:
        """Finds all the keys with a given prefix.

        This is essentially the same as the keys() function,
        but we start from the prefix node.

        Time: O(n*radix_length)+O(l) to find prefix node
        """
        keys = []
        prefix_node = self._get(self._root, prefix, 0, )
        self._traverse_tree(prefix_node, prefix, keys)
        return keys

    def longest_prefix(self, key: str) -> str:
        """Returns the longest prefix that matches the key.

        For example:
            Key: [Dog, Doge]
            Search for: [Dogegle]
            Returns: [Doge]

        1. If node is null, return the length
        2. If the node has a value, update length to be length search so far
        3. Get the child index for the char at this step.
        4. Recurse with next chr in the key at child node.
            (Step through key and down trie.)

        Time: O(n), where N is the length of the search key.
        """
        longest_key_len = self._get_longest(self._root, key, 0, 0)

        return key[:longest_key_len]

    def _get_longest(self, node: Node, key: str, key_index: int, length: int) -> int:
        """Recursive helper function."""
        if not node:
            return length

        if node.val:
            # We hit a word in this search
            length = key_index

        if key_index == len(key):
            # We hit the end of our key
            return length

        child_index = ord(key[key_index])

        return self._get_longest(node.children[child_index], key, key_index + 1, length)
