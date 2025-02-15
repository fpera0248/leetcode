from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # Dictionary to store grouped anagrams

        for word in strs:
            sorted_word = ''.join(sorted(word))  # Sort characters in word

            res[sorted_word].append(word)  # Group by sorted version

        return list(res.values())  # Convert dictionary values to a list of lists