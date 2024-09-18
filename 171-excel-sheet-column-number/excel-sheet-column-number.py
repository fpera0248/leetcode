class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        U:
        A-Z(1-26), AA is 27 AB 28 etc

        Empty String: return 0

        Best case: AE - 32

        Worst case: ZZZZZ - 12345

        A - 1
        AA  - 27

        As the letters move in indice, 26 gets added to its original total

        M:
        brute force: indice that letters are on matters - 2 for loops, 1 checking the indice, and one adding the values to a running tally - 0(n)

        dictionary, where i would add a ,z to dicitonary, then based on its indice, add the value of the orginal + 26 if indicie not 0


        P:
        if s is empty, 0

        create value pair in dicitonary, everything is upper case
        create a variable to store value
        use loops, one tracking the indice adding total values

        I:
        '''

        if not columnTitle:
            return 0

        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        counter = 1
        dictionary = {}

        for letter in list(alphabet):
            dictionary[letter] = counter
            counter += 1

        res = 0
        lst = list(columnTitle)

        for value in range(len(lst) - 1):
            if lst[value].isalpha() and lst[value] in dictionary:

                if len(lst) == 1:
                    return 1

                elif len(lst) > 1:
                    res += (dictionary[lst[value]] * 26 ** (len(lst) - value - 1))

        res += dictionary[lst[-1]]
        
        return res