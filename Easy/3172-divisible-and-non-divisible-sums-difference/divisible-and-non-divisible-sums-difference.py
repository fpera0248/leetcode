class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        num1_arr, num2_arr = [], []

        for i in range(n + 1):
            if i % m == 0:
                num2_arr.append(i)
            else:
                num1_arr.append(i)

        return sum(num1_arr) - sum(num2_arr)