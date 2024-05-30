from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.linkedList = OrderedDict()

    def put(self, key, value):
        if key in self.linkedList:
            self.linkedList.move_to_end(key)
        else:
            if len(self.linkedList) == self.capacity:
                self.linkedList.popitem(last=False)
        self.linkedList[key] = value
    
    def get(self, key):
        if key not in self.linkedList:
            return -1
        
        self.linkedList.move_to_end(key)
        return self.linkedList[key]
    

    
def main():
    # Create an LRU cache with capacity 2
    cache = LRUCache(2)

    # Test putting items in the cache
    cache.put(1, 1)       # Cache is {1=1}
    cache.put(2, 2)       # Cache is {1=1, 2=2}
    print(cache.get(1))   # Returns 1, Cache is {2=2, 1=1}
    cache.put(3, 3)       # LRU key 2 is evicted, Cache is {1=1, 3=3}
    print(cache.get(2))   # Returns -1 (not found)
    cache.put(4, 4)       # LRU key 1 is evicted, Cache is {3=3, 4=4}
    print(cache.get(1))   # Returns -1 (not found)
    print(cache.get(3))   # Returns 3, Cache is {4=4, 3=3}
    print(cache.get(4))   # Returns 4, Cache is {3=3, 4=4}


# Use orderedDict for O(1) time complexity for reordering operations such as move_to_end and popitem.
if __name__ == "__main__":
    main()