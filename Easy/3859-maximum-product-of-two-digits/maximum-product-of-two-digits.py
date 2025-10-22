class Solution:
    def maxProduct(self, n: int) -> int:
        
        w = (list(str(n)))     # ['1', '2', '3']
        w.sort(reverse=True)
        return int(w[0]) * int(w[1])