class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        track = []
        res = 1  # current consecutive count

        # Iterate through the string, comparing each character with the next
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                res += 1
            else:
                track.append(res)
                res = 1  # reset to 1 (the current character starts a new sequence)
                
        # Append the count for the final sequence
        track.append(res)
        
        return max(track)