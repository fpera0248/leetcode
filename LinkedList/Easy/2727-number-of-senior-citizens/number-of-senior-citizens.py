class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        '''
        U:
        string is length 15, details is a list of many strings size 15
        first 10 characters phone number
        next character is gender
        next two are age
        last two are seat allotment

        retrn passengers older than 60

        Input: list
        Output: int


        Good Case:
        Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
        Output: 2

        Bad Case:
        details = []

        return 0

        M:
        string iteration: iterate through details with double for loop

        
        P:

        brute force: double for loop, count values [:10], track people odler than 60 and return total people older than 60 (n^2 operation)

        details = ["7868190130M7522","5303914400F9211","9273338290F4010"]

        effective: cut all strings down to only age using slicing in python [:], check if value greater than 60 and output total int 0(n) operation

    
        I:
        '''
        res = 0
        age_list = []

        for age in details:
            age_list.append(age[11:13])

        count = 0

        for res in age_list:
            if int(res) > 60:
                count += 1
        return count



        '''

        R:


        E:





        '''