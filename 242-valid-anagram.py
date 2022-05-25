class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}
        
        for i in s:
            if i not in res.keys():
                res[i] = 1
            else:
                res[i] += 1
                
        for i in t:
            if i not in res.keys():
                return False
            else:
                res[i] -= 1
                
        for i in res.keys():
            if res[i] != 0:
                return False
        
        return True