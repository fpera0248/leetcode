class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        int arr nums, int k, return k most freqeuent elements
        
        Counter, occurrences of a int, 
        
        nums = [1,1,1,2,2,3]
        
        1: 3, 2: 2 3: 1
        
        res = []
        '''
        
        res = []
        
        digits = Counter(nums)
    
        for key, value in digits.most_common():
            res.append(key)
        return res[0:k]