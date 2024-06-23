class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        U:
        Input: s = "the sky is blue"
        Output: "blue is sky the"

        Input: s = "  hello world  "
        Output: "world hello"

        Input: s = "a good   example"
        Output: "example good a"


        M:
        string problem, 

        P:
        if word is a char, track the letters that form a word, 
        reversed index and find the characters, add that to new string, reverse it so that it is correctly  spelled, and add it to the 

        if word is char():
            add counter of letters: 
            then add new[:-counter], then add space, then ad next word, new[-counter:value]

        OR

        use split to combine the words, then join to remove spaces, then reverse index to add words to new list with spaces, 
        '''

        s = s.split()
        new_s = s[::-1]

        new_s = " ".join(new_s)
        return(new_s)