class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # Fix: Store as an instance variable
        self.capacity = capacity  # Fix: Store max capacity
        self.order = []  # Track key usage order

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move key to the most recently used position
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the key and move it to the most recently used position
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used key (first in order)
            lru_key = self.order.pop(0)
            del self.cache[lru_key]

        # Add new key-value pair
        self.cache[key] = value
        self.order.append(key)  # Track as most recently used