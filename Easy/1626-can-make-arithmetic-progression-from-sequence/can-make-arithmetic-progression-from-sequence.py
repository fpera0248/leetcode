class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()

        res = []

        for i in range(len(arr)-1):
            res.append(arr[i+1] - arr[i])

        if all(x == res[0] for x in res):
            return True
        return False