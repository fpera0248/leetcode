class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''
        unsorted arr int, 
        
        longest consecutive sequence
        
        nums = [3,7,2,5,8,4,6,0,1]
        
        use hashmap, keep track of values, track smallest value
        
        res = (sequence values)
        for i in hashmap:
            if smallest + 1 in hashmap:
        '''  
        
        
        # # ind = 0
        # # for ele in u:
        # #     print(ele)
        # #     if ind == 0:
        # #         count = 1
        # #         ans = 1
        # #         prev = ele
        # #     else:
        # #         if (prev+1)==ele:
        # #             count+=1
        # #             ans = max(ans,count)
        # #             prev = ele
        # #         else:
        # #             count  = 1
        # #             prev = ele
        # # return ans                
                   
        
        # # hashap = {}
        # # hashmap2[4] = 
        # # uinque = set(nums)
        # # 0
        # # /* 
        # #    hashmap[3] = 4
        # #    dp[3] ///the length of longest consecutive elemnts if the sequnces starts with 3
        # #    index 0 ----
        # #    100,,,
        # #    dp[100] = 1 + dp[101]
        # #    rec(index 4)
        #           dp[101]
        
           
           
           
        
        # # */
        # if not nums:
        #     return 0
            
        # res = []
        # lowest = min(nums)
        # counter = 1
        # hashmap = {}
        #101----------if 101 is not hashmap
        # for i in range(len(nums)):
        #     hashmap[i] = nums[i]

        # for _ in range(len(nums)):
        #     if (lowest + 1) in hashmap.values():
        #         counter += 1
        #         lowest += 1

        #     else:
        #         res.append(counter)
        #         lowest += 1
        #         counter = 1
        # res.append(counter)
        # return max(res)             
        hashmap = {}
        uique = set(nums)
        newList = [ele for ele in uique]
        for i in range(len(newList)):
             hashmap[newList[i]] = -1
             hashmap[newList[i] + 1] = -1
        for i in range(len(newList)):
             hashmap[newList[i]] = i
        dp = [-1 for ele in newList]
        def rec(i):
            curVal = newList[i]
            if hashmap[curVal + 1] == -1:
                dp[i] = 1
            else:    
                index = hashmap[curVal + 1]
                rec(index)
                dp[i] = 1 + dp[index]      
        for i in range(len(newList)):
             if dp[i] != -1: 
                continue
             else:
                 rec(i)    
        if dp:
            return max(dp)
        return 0    
        # return (dp ? max(dp) : 0)
        
         
            
                    
        
                
        
       
        