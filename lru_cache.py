class Node:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}
        self.counter = 0
        self.head = Node(0, 0)
        self.tail = Node(1, 1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        n = self.hm[key]

        self.extract(n)
        self.putAsLatest(n)
        return n.val

    def extract(self, n):
        pre = n.prev
        post = n.next
        pre.next = post
        post.prev = pre

    def putAsLatest(self, n):
        n.prev = self.tail.prev
        n.next = self.tail
        self.tail.prev.next = n
        self.tail.prev = n

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            n = self.hm[key]
            self.extract(n)
            self.putAsLatest(n)
            n.val = value
            return

        if self.counter >= self.cap:
            n = self.head.next
            del self.hm[n.key]
            self.head.next = n.next
            n.next.prev = self.head
            n.next = None
            n.prev = None
            self.counter -= 1

        n2 = Node(key, value)
        self.hm[key] = n2

        self.putAsLatest(n2)
        self.counter += 1
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Problem 1: LRU Cache
# Using OrderedDict from collections library as it maintains the ordered of operations
# Time Complexity is O(1) for all operations
# Space Complexity is O(n) where n= capacity of our Cache

from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.hm = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.hm:
            return -1

        val = self.hm[key]
        del self.hm[key]
        self.hm[key] = val
        return val

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # Checking the key in hm ensures that we are not removing an entry from cache
        # if it is already included and length == capacity
        if key in self.hm:
            self.get(key)

        self.hm[key] = value

        # Easier to ask forgiveness than permission
        if len(self.hm) > 3:
            self.hm.popitem(last=False)


our_cache = LRU_Cache(1)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # return -1


