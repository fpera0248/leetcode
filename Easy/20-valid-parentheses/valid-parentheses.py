class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for char in s:
            if char in hashmap:  # opening bracket
                stack.append(char)
            else:  # closing bracket
                if not stack or hashmap[stack.pop()] != char:
                    return False

        return not stack