class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        
        two = set(friends)
        res = []

        for i in order:
            if i in two:
                res.append(i)

        return res