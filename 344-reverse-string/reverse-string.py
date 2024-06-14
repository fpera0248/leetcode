class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        U:
        reverse string in place

        M:
        two pointer (start and end), string traversal

        P:
        create two pointers one at start one at end, remove values in place, 

        for h","e","l","l","o"

        pointer at p pointer at o
        create tracker variable that stores the value of h before it is move to the end

        I:

        '''

        start, end = 0, len(s)-1

        while start <= end:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp

            start += 1
            end -= 1