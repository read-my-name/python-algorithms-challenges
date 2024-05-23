from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.key_to_frequency = defaultdict(int)  # Keeps track of the frequency of each key.
        self.frequency_to_keys = defaultdict(lambda: OrderedDict())  # Keeps track of keys with the same frequency, stored in an ordered manner.
        self.capacity = capacity  # Maximum capacity of the cache.
        self.min_frequency = 1  # Minimum frequency of keys in the cache.

    def get(self, key: int) -> int:
        if key not in self.key_to_frequency:
            return -1
        frequency = self.key_to_frequency[key]
        self.key_to_frequency[key] += 1
        value = self.frequency_to_keys[frequency][key]
        del self.frequency_to_keys[frequency][key]
        self.frequency_to_keys[frequency + 1][key] = value
        if self.min_frequency == frequency and not self.frequency_to_keys[frequency]:
            self.min_frequency += 1
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_frequency:
            self.get(key)
            self.frequency_to_keys[self.key_to_frequency[key]][key] = value
        else:
            self.capacity -= 1
            self.key_to_frequency[key] = 1
            self.frequency_to_keys[1][key] = value
            if self.capacity < 0:
                k, v = self.frequency_to_keys[self.min_frequency].popitem(False)
                del self.key_to_frequency[k]
                self.capacity += 1
            self.min_frequency = 1

def main():
    # Create an instance of LFUCache with capacity 3
    cache = LFUCache(3)

    # Perform some put and get operations
    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(3, 30)
    print("Cache state after initial put operations:")
    print(cache.key_to_frequency)
    print(cache.frequency_to_keys)
    print("Minimum frequency:", cache.min_frequency)

    # Access key 1 twice
    cache.get(1)
    cache.get(1)
    print("\nCache state after accessing key 1 twice:")
    print(cache.key_to_frequency)
    print(cache.frequency_to_keys)
    print("Minimum frequency:", cache.min_frequency)

    # Access key 2 and key 3
    cache.get(2)
    cache.get(3)
    print("\nCache state after accessing keys 2 and 3:")
    print(cache.key_to_frequency)
    print(cache.frequency_to_keys)
    print("Minimum frequency:", cache.min_frequency)

    # Add a new key-value pair
    cache.put(4, 40)
    print("\nCache state after adding key 4:")
    print(cache.key_to_frequency)
    print(cache.frequency_to_keys)
    print("Minimum frequency:", cache.min_frequency)

    # Access key 1, which was accessed twice previously
    cache.get(1)
    print("\nCache state after accessing key 1 again:")
    print(cache.key_to_frequency)
    print(cache.frequency_to_keys)
    print("Minimum frequency:", cache.min_frequency)


# Execute the main function
if __name__ == "__main__":
    main()

#self.key_to_frequency = defaultdict(int)  # Keeps track of the frequency of each key.
#self.frequency_to_keys = defaultdict(lambda: OrderedDict())  # Keeps track of keys with the same frequency, stored in an ordered manner.

# # Initialize LFUCache with capacity 2
# cache = LFUCache(2)

# # Put key='a', value=1
# cache.put('a', 1)
# # Cache: {'a': 1}, key_to_frequency: {'a': 1}, frequency_to_keys: {1: {'a': 1}}, min_frequency: 1

# # Put key='b', value=2
# cache.put('b', 2)
# # Cache: {'a': 1, 'b': 2}, key_to_frequency: {'a': 1, 'b': 1}, frequency_to_keys: {1: {'a': 1, 'b': 2}}, min_frequency: 1

# # Put key='c', value=3 (capacity exceeded, evict least frequently used)
# cache.put('c', 3)
# # Cache: {'b': 2, 'c': 3}, key_to_frequency: {'b': 1, 'c': 1}, frequency_to_keys: {1: {'b': 2, 'c': 3}}, min_frequency: 1

# # Get key='b' (update frequency)
# cache.get('b')
# # Cache: {'b': 2, 'c': 3}, key_to_frequency: {'b': 2, 'c': 1}, frequency_to_keys: {1: {'c': 3}, 2: {'b': 2}}, min_frequency: 1

# # Put key='d', value=4 (capacity exceeded, evict least frequently used)
# cache.put('d', 4)
# # Cache: {'b': 2, 'd': 4}, key_to_frequency: {'b': 2, 'd': 1}, frequency_to_keys: {1: {'d': 4}, 2: {'b': 2}}, min_frequency: 1
