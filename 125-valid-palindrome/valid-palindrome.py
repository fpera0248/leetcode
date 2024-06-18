class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ''.join(filter(str.isalnum, s)).lower()

        p1 = 0
        p2 = len(cleaned_string) - 1

        print(cleaned_string)
        while p1 < p2:
            if cleaned_string[p1] != cleaned_string[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        return True
