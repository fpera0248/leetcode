class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
    
        #populate it using the elements in arr
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        freq_set = set()
        
        for value in hashmap.values():
            if value in freq_set:
                return False
            freq_set.add(value)
        return True