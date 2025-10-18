def helper(flips,x):
     if flips%2 == 0:
          return x
     else :
         if x=='0': 
            return '1'
         return '0'        
class Solution :
    def minFlips(self, target: str) -> int:
        n = len(target)
        flips = 0
        operations = 0
        for i in range(n):
            newValue = helper(flips,'0');
            if newValue != target[i]:
                flips+=1
                operations+=1
        return operations        
        
    
        
        
        