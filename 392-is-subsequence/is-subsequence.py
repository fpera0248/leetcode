class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        U:
        Input: s = "abc", t = "ahbgdc"
        Output: true

        M:
        could be two pointers

        s = "abc", t = "ahbgd"
               i            j

        P:
        set up two pointers, one for list s and to check the occurences of the values in order in list t
        if values dont occur in same order, return false else true
           '''

        i, j = 0, 0
        counter = len(s)

        while j <= len(t) - 1 and i <= len(s) - 1:
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
                counter -= 1
            
        if counter == 0:
            return True    
        return False

        '''
        E:
        Time:
        0(n)

        Space:
        0(1)
        '''
        