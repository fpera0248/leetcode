class Solution:
    def firstUniqChar(self, s: str) -> int:


        hashmap = {}
        queue = []

        # Populate the hashmap with character counts
        for value in s:
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1

            queue.append(value)

        # Iterate over the characters in the queue
        for unique in range(len(queue)):
            if hashmap[queue[unique]] == 1:
                return unique
        
        # If no unique character is found, return -1
        return -1