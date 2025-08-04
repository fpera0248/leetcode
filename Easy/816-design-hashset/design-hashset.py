class MyHashSet(object):

    def __init__(self):
        
        self.MyHashSet = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        
        if key not in self.MyHashSet:
            self.MyHashSet.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """

        if key in self.MyHashSet:
            self.MyHashSet.remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        
        if key in self.MyHashSet:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)