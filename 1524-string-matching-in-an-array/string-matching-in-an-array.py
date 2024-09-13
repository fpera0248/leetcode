class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        '''
        U:
        return substring of any words
        substrings are shorter in length than their original strings
        substring contains characters in same sequence
        words can be substrings of the ssame words
        return list of strings with all of the substrings

        Cases:
        if empty string, return []


        M:
        dictionary - possible but not effective
        not stack or queue
        
        P:
        divide the list up by length, substring would be in front
        leetcode,

        check if et is a string sequence in order in my stack [:2]
        make into 2d array, where 1 indice is word and other is substring


        '''
        new=[]
        for w in words:
            for i in words:
                if w in i and w!=i:
                    new.append(w)
                    break
        return new

