class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        '''
        U:
        sentence = str
        searchWord = str
        return = int

        sentence empty return 0

        M:

        string manipulation: 
        fidn if the searchword is aprefix of anything


        use splcigin [:searchWord] to figure out if search word is a prrefix to another word

        is searchword is burg , lenght 4, search the arr to see

        '''

        for index, value in enumerate(sentence.split()):
            if len(value) >= len(searchWord):
                if value[:len(searchWord)] == searchWord:
                    return index + 1
        return -1

