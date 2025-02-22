class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        product, addition = 1, 0

        for i in str(n):
            product *= int(i)
            addition += int(i)

        return(product-addition)
