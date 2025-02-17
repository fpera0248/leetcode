class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        '''
        U:
        startTime: array
        endTime: array
        queryTime: int
        Output: int

        Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
        Output: 1

        Input: startTime = [4], endTime = [4], queryTime = 4
        Output: 1

        Bad case:

        if startTime empty:
            return 0

        M:
        array, traversal problem -> check both arrays for when their equal to query time 0(n)

        P:
        if not startiem:
            reutrn 0

        value to track the students that fall within the queryTime

        track end time greater than or equal to 4

        reutnr tracker

        '''

        if not startTime:
            return 0
        
        res = 0
        tracker = 0

        for index, value in enumerate(startTime):
            if value <= queryTime:
                tracker = index

                if endTime[tracker] >= queryTime:
                    res += 1
        return res