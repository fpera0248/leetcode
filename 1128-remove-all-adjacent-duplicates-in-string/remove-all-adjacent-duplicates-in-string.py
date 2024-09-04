class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        U:
        remove adjacent dups in a string
        abbaca, turns in to ca

        aaaaaac, turns in to c
        abbbctr, abctr

        M:
        stack, append values to the stack (lifo)

        P:
        change string into different data type to edit it
        add letters to the stack, if the same letter is added twice in a row, use the pop method twice to remove that letter
        track the occurrences of the strings using variable for previous letter
        return stack values as a str value, once you pop start at beginning of array

        I:
        '''

        stack = []
        s_list = list(s)
        
        # Initialize previous character and push it to the stack
        prev = s_list[0]
        stack.append(prev)
        
        for i in range(1, len(s_list)):
            if stack and stack[-1] == s_list[i]:
                # If the current character is the same as the top of the stack, pop the stack
                stack.pop()
                # If the stack is not empty after popping, update prev to the new top of the stack
                prev = stack[-1] if stack else None
            else:
                # Otherwise, push the current character to the stack and update prev
                stack.append(s_list[i])
                prev = s_list[i]

        # Join the stack to form the resulting string
        return "".join(stack)
