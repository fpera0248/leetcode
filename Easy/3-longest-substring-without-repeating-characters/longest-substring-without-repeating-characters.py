class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        res = 0
        counter = 0

        if not s:
            return 0
        
        left = 0  # new pointer to track where substring starts
        
        for right in range(len(s)):
            while s[right] in seen:              # remove duplicates
                seen.remove(s[left])
                left += 1
                counter -= 1                     # shrink window count

            seen.add(s[right])
            counter += 1
            res = max(res, counter)              # update result

        return res