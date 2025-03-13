class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
        k = k % len(s)  # Handle cases where k is larger than len(s)
        return s[k:] + s[:k]  # Perform a left rotation
