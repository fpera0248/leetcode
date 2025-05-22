class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        # Loop through the length of the shorter word
        while i < len(word1) and i < len(word2):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
        # Append the rest of the longer word
        merged.append(word1[i:])
        merged.append(word2[i:])
        return ''.join(merged)

            
        
        