from typing import Any, Dict

# Default cache capacity.
# Once this is exceeded, values will start being popped.
_DEFAULT_CAPACITY = 100


class Node:
    """Node for used in LruCache.

    This of this like a doubly-linked list node combined
    with a hash map node.
    We have key-val, and also next-previous.
    """

    def __init__(self, key: Any = None, val: Any = None) -> None:
        """Initializes node class."""
        self.key = key
        self.val = val
        self.next = None
        self.previous = None


class LruCache:
    """An LRU cache implementation.

    The LRU cache allows objects to be added/removed in constant time.
    * When an item is retrieved or added, it becomes the most recently used.
    * If the cache becomes full, the least recently used item is removed.

    To get and put in constant time, we use a hash map.
    To keep track of the most/least recently used, we use a doubly linked list,
    and 2 pointers.
    The hash map points to nodes in our doubly linked list.

    LRU <> [our values] <> MRU

    Time:
    * Get: O(1) average, O(n) worst case
    * Put: O(1) average, O(n) worst case
    """
    def __init__(self, capacity: int = _DEFAULT_CAPACITY) -> None:
        """Initializes the LRU Cache."""
        self.size = 0
        self._capacity = capacity
        self._cache: Dict[Any, Node] = {}

        self._most_recently_used = Node()
        self._least_recently_used = Node()

        self._most_recently_used.previous = self._least_recently_used
        self._least_recently_used.next = self._most_recently_used

    def add(self, key: Any, val: Any) -> None:
        """Adds a key/value to the cache.

        1. If the key is not in the cache:
            1.1 If we are >= capacity...
                * Get the LRU node.
                * deleted the oldest node from the cache and decrement size.
            1.2 Create a new node.
            1.3 Set the key/val in the cache.
            1.4 Set this as the MRU.
        2. If the key is in the cache:
            2.1 Update the value of the cached node.
            2.2 Remove the cached node.
            2.3 Set it as most recently used.

        Time: O(1) average, O(n) worst case

        :param key: The key to add.
        :param val: The value to add for this key.
        :return: None.
        """

        if key not in self._cache:
            # Add a new node
            if self.size >= self._capacity:
                oldest = self._pop_least_recently_used()
                del self._cache[oldest.key]
                self.size -= 1

            new_node = Node(key, val)
            self._cache[key] = new_node
            self._set_most_recently_used(new_node)
            self.size += 1
        else:
            # Node already exists
            cached_node = self._cache[key]
            cached_node.val = val
            _remove_node(cached_node)
            self._set_most_recently_used(cached_node)

    def _pop_least_recently_used(self) -> Node:
        """Removes and returns the least recently used node.

        1. Get the least recently used node.
        2. Remove it.
        3. Return it.

        Time: O(1)

        :return: The lease recently used node in the cache.
        """
        oldest = self._least_recently_used.next
        _remove_node(oldest)

        return oldest

    def _set_most_recently_used(self, node: Node) -> None:
        """Sets a node to be the most recently used.

        1. Grab the old most recently used node.
        2. Update the new node's pointers:
           2.1 Set previous to be the old most recently used.
           2.2 Set next to be most recently used.
        3. Update old most recently used's next to be new node.
        4. Set most recently used's prev to be new node.


        [Least recently used] <> 1 <> 2 <> [3] <> [Most recently used]
                                      ^ New MRU

        [Least recently used] <> 1 <> [3] <> 2 <> [Most recently used]
                                             ^ New MRU

        Even in a size==1 cache, the node will be set in the middle.

        Time: O(1)

        :param node: The node to set as the most recently used.
        :return: None.
        """
        old_most_recently_used = self._most_recently_used.previous

        # Update new node's pointers
        node.previous = old_most_recently_used
        node.next = self._most_recently_used

        # Update old node's pointers
        old_most_recently_used.next = node

        # Update most recently used pointer
        self._most_recently_used.previous = node

    def get(self, key: Any) -> Any:
        """Gets a value from the cache based on the key.

        1. Check the key exists.
        2. Get the node from the cache.
        3. Remove it from the cache.
        4. Set it to be the most recently used node.

        Time: O(1) average, O(n) worst case.

        :param key: The key to retrieve.
        :return: The value associated with this key.
        """
        if key not in self._cache:
            raise KeyError('Key not found!')

        cached_node = self._cache[key]

        _remove_node(cached_node)
        self._set_most_recently_used(cached_node)

        return cached_node.val


def _remove_node(node: Node) -> None:
    """Removes a node.

    1. Grab the previous node.
    2. Grab the next node.
    3. Set previous and next to point to each other,
       therefore removing the node in the middle.

    Time: O(n)

    :param node: The node to remove.
    :return: None.
    """
    previous = node.previous
    next_node = node.next

    previous.next = next_node
    next_node.previous = previous
