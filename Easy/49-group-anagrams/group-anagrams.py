class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []

        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        for group in hashmap.values():
            res.append(group)

        return res
