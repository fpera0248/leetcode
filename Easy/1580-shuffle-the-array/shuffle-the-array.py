class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        '''
        where 2n /2 that indice starts the y section, deviide these section then pull an element from each to a new res arr

        2 pointers starting at 2n/2


        '''

        res = []

        x, y = 0, n

        for _ in range(y, len(nums)):

            res.append(nums[x])
            res.append(nums[y])

            x += 1
            y += 1

        return res
