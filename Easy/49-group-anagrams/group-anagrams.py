class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        helper = {}
        for st in strs:
             sortedVersion  = sorted(st)
             temp = ""
             for ele in sortedVersion:
                 temp = temp + ele
             sortedVersion = temp     
             if sortedVersion in helper:
                 helper[sortedVersion].append(st)       
             else:
                helper[sortedVersion] = [st]
        print(helper)
        return [ele for ele in helper.values()]               
                

