class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        

        '''
        input: 2d integer array 
        nums[i] is a list of dinstinct positive integers
        return integers that ar epresent in all

        if len of nums is 3, and a number occurs 3 times return that number 

        track occurences

        do a for loop for the indices then a sub foor loop for the values
        then track occurences of each number
        number that appears n length amount of times return as a list

        '''
        hashmap = {}
        length = len(nums)
        res = []

        for index in nums:
            for number in index:
                if number in hashmap:
                    hashmap[number] += 1
                else:
                    hashmap[number] = 1

        for key, value in hashmap.items():
            if value == length:
                res.append(key)

        return sorted(res)


                    
