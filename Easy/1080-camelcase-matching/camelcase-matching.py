def helper(inp,pattern):
    #  input = "FooBar" pattern = "FoBa"
    index = 0
    n = len(inp)
    for ch in pattern:
        while index<n and inp[index]!= ch:
            if inp[index]>='A' and inp[index]<='Z':
                 return False
            index+=1
        index+=1    
        if index>n :
           return False
    for i in range(index,n):
        if inp[i]>='A' and inp[i]<='Z':
                return False    
    return True       
     
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        '''
        input: arr of strings
        string pattern
        
        return: boolean arr where answer[i] == true if queries[i] matches pattern
        
        Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],      pattern = "FB"
        
        
        Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
        index i to index j
        helper(input,query)
        '''
        res = []
        for query in queries:
            res.append(helper(query,pattern))
        return res    
        