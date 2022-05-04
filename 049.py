class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        res = {}
        for i in strs:
            ind = str(sorted(i))
            if ind not in res.keys():
                res[ind] = [i]
            else:
                res[ind].append(i)
                
        return res.values()