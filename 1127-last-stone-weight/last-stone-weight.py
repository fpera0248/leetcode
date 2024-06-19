class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        [2,7,4,1,8,1]
        sort list

        [8,7,4,2,1,1]
        subtract p1 and p2
        stones[p1] - stones[p2] == stones[p1]
        remove [p2]

        [1, 4, 2, 1, 1]
        sort again

        4,2,1,1,1
        subtract

        2,1,1,1

        1,1,1

        if stones.len > 1:
        1
        '''
        if not stones:
            return 0

        length = len(stones)
        p1 = 0
        p2 = 1

        if length == 1:
            return stones[0]

        if length == 2:
            return abs(stones[0] - stones[1])

        while True:
            stones.sort(reverse=True)

            if length == 2:
                return abs(stones[p1] - stones[p2])

            if stones[p1] == stones[p2]:
                stones.pop(p1)
                stones.pop(p2 - 1)
                length -= 2
                p1 = 0
                p2 = 1
            else:
                stones[p1] -= stones[p2]
                stones.pop(p2)
                length -= 1

            if length == 1:
                return stones[0]

            if length == 0:
                return 0