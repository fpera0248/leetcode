class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        '''
        U:
        finding number of substrings of length k, that a divisible by k

        num 35000, k = 5
        if num empty, return num

        track total number of substrings that meet this constraints

        M:
        indice matching string problem

        P:
        check value of k, use slciing [:k] to iterate through the indices k at a time then check if those num is evenly divisible by k (num % k == 0)

        do while loop while len of k < remaining len of num:

        check the indicie values and return if it s a bustrings and matches k beauty standrd, if so add a variable for trackin gk beauty score
        return int k beauty score

        '''

        k_beauty = 0
        lst = list(str(num))  # Convert the number to a string, then to a list
        for i in range(len(lst) - k + 1):
            blocks = lst[i:i+k]
            block_as_int = int(''.join(map(str, blocks)))
            
            if block_as_int != 0:
                if num % block_as_int == 0:
                    k_beauty += 1
        return k_beauty