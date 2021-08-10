"""
Using linked list and hashmap together

Time complexity: O(N)
Space complexity: O(N)
"""


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    """
    Least Recently Used (LRU) cache
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity
        """
        self.cache = {}
        self.count = 0
        self.capacity = capacity

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        self.insert_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
        If the number of keys exceeds the capacity from this operation, evict the least recently used key.
        """
        node = self.cache.get(key, None)

        if not node:
            new_node = ListNode(key, value)

            self.cache[key] = new_node
            self.add_node(new_node)

            self.count += 1

            if self.count > self.capacity:
                tail = self.remove_tail()
                del self.cache[tail.key]
                self.count -= 1
        else:
            node.value = value
            self.insert_to_head(node)

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def insert_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def remove_tail(self):
        res = self.tail.prev
        self.remove_node(res)
        return res


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
