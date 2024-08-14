class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        '''
        U:
        return the max value in a string

        M:
        iteration

        P:
        use is alpharnumeric boolean statements
        if it is count the length of the value, if not use the vase 10 to calculate its value

        i:
        '''

        res = []

        for value in strs:
            if value.isnumeric():
                res.append(int(value))
            else:
                res.append(len(value))

        return max(res)