class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        tracker = 0
        
        # Check all possible substrings
        for i in range(n):
            for j in range(i + 1, n + 1):
                # If substring is palindrome, increment tracker
                if s[i:j] == s[i:j][::-1]:
                    tracker += 1
        
        return tracker