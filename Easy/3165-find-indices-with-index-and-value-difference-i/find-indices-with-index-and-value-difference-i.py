'''

U: 

i and j, that satifies both condiditions

return arr answer, where i,j are values 

if two indices cant match these conditions return [-1,-1]

P:

double for loop, iterate through list, if conditions are meet , add i and j to answer and return

if not [-1,-1]
'''
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        answer = []

        for i in range(len(nums)):
            for j in range(len(nums)):

                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    return [i,j]
        return [-1, -1]