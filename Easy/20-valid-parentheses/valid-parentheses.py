class Solution:
    def isValid(self, s: str) -> bool:
        '''
        if the list has odd amount of values, return false because it can't have closed parentheses for each one

        if list empty return false

        use a list as a stack, create dictionary with opening brackets as keys and closing as values
        if i have stack as a list, for every open parentheses I have, i need a matching closing parentheses, so once an open one is encountered remove closed one from stack, if no key available for closing , return false, if every bracket has a closing return true

        '''
        if not s:
            return False

        if len(s) % 2 != 0:
            return False

        stack = []

        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        for char in s:
            if char in brackets:  # If it's an opening bracket
                stack.append(brackets[char])
            elif not stack or char != stack.pop():  
                return False

        return len(stack) == 0 
