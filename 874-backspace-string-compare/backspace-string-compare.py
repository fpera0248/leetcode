class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

       # Initialize stacks for both strings
        stack_s = []
        stack_t = []

        # Process string s
        for char in s:
            if char == '#':
                if stack_s:
                    stack_s.pop()  # Remove the last character if it's a backspace
            else:
                stack_s.append(char)  # Otherwise, add the current character to the stack

        # Process string t
        for char in t:
            if char == '#':
                if stack_t:
                    stack_t.pop()  # Remove the last character if it's a backspace
            else:
                stack_t.append(char)  # Otherwise, add the current character to the stack

        # Compare the final processed results
        return ''.join(stack_s) == ''.join(stack_t)