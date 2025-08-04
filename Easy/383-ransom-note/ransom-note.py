class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        '''
        U:
        if letters in magazine in ransomnote, return true

        else false

        cases:
            empty string

        M:
        hashmap

        P:
        turn ransomnote and mag in to lists
        if all letters in ransom note in mag return true
        use for loop to iterate throguh and output

        I:

        '''

        if not ransomNote or not magazine:
            return False

        list_r, list_m = list(ransomNote), list(magazine)

        for letter in list_r:
            if letter in list_m:
                list_m.remove(letter)
            else:
                return False
        return True


        '''

        R:
    

        E:


        '''