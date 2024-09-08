class Solution:
    def clearDigits(self, s: str) -> str:
        '''
        U:
        remove first digit and the closest non digit cahracter to its left

        cb34
        c is not digit, move on
        b is not digit move on
        3 is digit, remove 3 and remove b since it is a non-digit character
        same with 4, then string is empty retunr empty sring

        M:
        stack

        P:
        if empty, return ''

        use stack to accomplish this

        add values to stack if theyre non-digit, once digit is encounter do not add it and pop the closest non-digit
        if no non-digit values exists to the left, continue the loop without removing anything.

        iterate through the string, turn string into list and add final values to a res list

        I:
        '''

        stack = []

        

        for digit in s:

            if not s:
                return ''

            if stack:
                peek = stack[-1]

            if digit.isalpha():
                stack.append(digit)
            elif digit.isdigit():
                if peek.isalpha():
                    stack.pop()

        return ''.join(stack)
            

