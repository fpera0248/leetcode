class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        arr = []
        while nums:
            # Alice removes the smallest
            alice_pick = min(nums)
            nums.remove(alice_pick)
            
            # Bob removes the next smallest
            bob_pick = min(nums)
            nums.remove(bob_pick)
            
            # Bob appends his pick first, then Alice
            arr.append(bob_pick)
            arr.append(alice_pick)
        
        return arr

            

