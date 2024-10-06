class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        '''
        U:
        find all occurences of the third word given the first two


        M:
        


        P:


        I:

        '''
        if not text:
            return 0

        res = []
        split_list = (text.split())

        for i in range(len(split_list) - 2):
            if split_list[i] == first and split_list[i+ 1] == second:
                res.append(split_list[i+2])
        return res


        '''


        R:


        E:




        '''