class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        
        one, two = set(order), set(friends)
        res = []

        for i in order:
            if i in two:
                res.append(i)

        return res