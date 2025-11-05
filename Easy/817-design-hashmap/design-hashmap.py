class MyHashMap:
    store = {}
    def __init__(self):
        self.store = {}

    def put(self, key: int, value: int) -> None:

         self.store[key] = value

    def get(self, key: int) -> int:
        # print(list(self.store.keys()))
        if key in list(self.store.keys()) :     
            return self.store[key]
        return -1

    def remove(self, key: int) -> None:
        
        self.store[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)