class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        '''
        U:

        int arr: target, int n

        return string list

        return stack operations needed for stack to equal target

        if stream 1 to n, push value to top of stack
        if stack, pop top of stack

        worst caseL
        empty target, or n = 0

        best case: 

        constraints: 
        1 <= target.length <= 100
        1 <= n <= 100
        1 <= target[i] <= n
        target is strictly increasing.

        M:
        stack operations: o(n)

        I:
        if len(target) == 1

        stack = []
        res = ["Push"]

        stack.append(1)

        top of stack is stack[::-1]

        if next value in target if less than the value we pushed, pop the value and continue
        track = 1

        for i in range(2, n):

            stack.push(i)
            res.append('Push')

            if target[track] == i:
                continue
            stack.pop(i)

            if target == stack:
                return res
        '''

        if len(target) == 1:
            return ['Push']

        stack = []
        res = []
        track = 0

        for i in range(1,  n+1):

            stack.append(i)

            print(stack)
            res.append('Push')

            if target[track] == i:
                track += 1
            else:
                stack.remove(i)
                res.append('Pop')
              

            print(res)

            if target == stack:
                return res
