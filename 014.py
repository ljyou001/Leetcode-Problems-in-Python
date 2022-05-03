class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        
        for i in range(len(strs[0])):
            chara = strs[0][i]
            for j in strs: 
                if i == len(j) or j[i] != chara:
                    return strs[0][0:i]
        return strs[0]