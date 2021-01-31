from typing import Any

# Typically set to power or two or prime number
_ARRAY_SIZE = 97


class Node:

    def __init__(self, key: Any, val: Any, next_node):
        self.key = key
        self.val = val
        self.next = next_node


class HashMap:
    """A hash map implemented with chaining.

    Cf. open addressing (used by Python). Open addressing is more
    memory efficient, but could end up having to readdress
    everything if the array requires resizing, since the
    hash algorithm requires the addresses to be of fixed size.
    Therefore, even though we may have "wasted space", this
    behaves more gracefully as the array fills up.

    Operations:
    * Put(key, val): O(1) avg, O(n) worst case (collisions)
    * Get(key): O(1) avg, O(n) worst case
    * Remove(key): O(1) avg, O(n) worst case
    * Contains(key): O(1) avg, O(n) worst case
    """
    def __init__(self, size: int = _ARRAY_SIZE):
        """Initialize the array with a default size."""
        self._arr = [None] * size
        self.size = 0

    def put(self, key: Any, val: Any):
        """Adds a key and value to the hash map.

        1. Get the hash (index)
        2. Get the node at that index
        3. While it's not null...
            3.1 If the key matches, just update the value (key already exists)
        4. Set the node at this index to be key, val, and the node at this index if it exists
           (i.e., add it to the front of the linked list)

        Time: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        node = self._arr[index]

        while node:
            if node.key == key:
                # Updating an existing key
                node.val = val
                return
            node = node.next

        self.size += 1
        self._arr[index] = Node(key, val, self._arr[index])

    def contains(self, key: Any) -> bool:
        """Returns True if key exists in map"""
        index = self._hash(key)
        node = self._arr[index]

        while node:
            if node.key == key:
                return True
            node = node.next

        return False

    def get(self, key: Any) -> Any:
        """Returns the value for this key."""
        index = self._hash(key)
        node = self._arr[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next

        raise KeyError('Key not found!')

    def delete(self, key: Any) -> None:
        """Deletes a key from the hash map in a recursive fashion.

        1. Get the node at this index.
        2. Call the delete function with this node and key.
            2.1 If the node is null, raise a KeyError.
            2.2 If the node.key == key, return next node.
            2.3 Set node.next to a call with node.next
            2.4 Return the node.

        Time: O(1) average, O(n) worst case.
        """
        index = self._hash(key)
        self._arr[index] = self._delete(self._arr[index], key)

    def _delete(self, node: Node, key: Any) -> Node:
        """Delete helper method."""
        if not node:
            raise KeyError('Key not found!')

        if key == node.key:
            self.size -= 1
            return node.next

        node.next = self._delete(node.next, key)
        return node

    def _hash(self, key: Any) -> int:
        """Gets a hash index to add the item to in the array.

        * Take the abs value of the key's hash, then the modulus
          of the array size.

        :param key: The key to add to the hash map.
        :return: The position in the array to add the item.
        """
        return abs(hash(key)) % len(self._arr)
