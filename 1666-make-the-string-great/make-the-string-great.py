class Solution:
    def makeGood(self, s: str) -> str:
        '''
        U:
        string of upper and lower case letters
        a good string, does not have adjacent characters of different case (upper and lower)
        remove these bad characters, and return string once it is good
        empty string is also good

        M:
        stack
        two pointers

        P:
        create an empty stack, make a copy of string and turn in to list, add values to stack,
        if i and i + 1 are the same letter but different case, do not add to stack,
        at end turn list into string again(.join''(str(list))
        '''

        stack = []

        def peek():
            return stack[-1] if stack else None
    
        stack.append(s[0])

        for i in range(1, len(s)):
            top = peek()

            if top and top.lower() == s[i].lower() and top != s[i]:
                stack.pop()  # Remove the last character if it's a bad pair
            else:
                stack.append(s[i])  # Otherwise, add the current character to the stack

        return ''.join(stack)  # Join the stack to form the resulting "good" string