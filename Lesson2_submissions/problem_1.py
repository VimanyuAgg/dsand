# Problem 1: LRU Cache
# Using OrderedDict from collections library as it maintains the ordered of operations
# Time Complexity is O(1) for all operations
# Space Complexity is O(n) where n= capacity of our Cache

from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity=None):
        ''' Initialize class variables '''
        self.capacity = capacity
        self.hm = OrderedDict()

    def get(self, key):
        '''Retrieve item from provided key. Return -1 if nonexistent.'''
        if key not in self.hm:
            return -1

        val = self.hm[key]
        del self.hm[key]
        self.hm[key] = val
        return val

    def set(self, key, value):
        '''set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.'''

        # Sanity check
        if (not self.capacity) or self.capacity <= 0:
            return

        # Checking the key in hm ensures that we are not removing an entry from cache
        # if it is already included and length == capacity
        if key in self.hm:
            self.get(key)

        self.hm[key] = value

        # Easier to ask forgiveness than permission
        if len(self.hm) > self.capacity:
            self.hm.popitem(last=False)


# Test Case 1
our_cache2 = LRU_Cache() # Null capacity
our_cache2.set(1, 1)
our_cache2.set(2, 2)

print(our_cache2.get(2))
# returns -1
print(our_cache2.get(3))
# return -1


# Test Case 2
our_cache = LRU_Cache(2)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(1, 2)

print(our_cache.get(1))
# returns 2

print(our_cache.get(2))
# returns -1

print(our_cache.get(3))
# return 3

# Test Case 3
our_cache = LRU_Cache(3)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 18)
our_cache.set(1, 28)
our_cache.set(1, 2)

print(our_cache.get(1))
# returns 2

print(our_cache.get(2))
# returns 2

print(our_cache.get(3))
# return -1



