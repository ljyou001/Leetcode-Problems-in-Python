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

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        res = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(len(strs)):
                if i >= len(strs[j]):
                    return res
                if char != strs[j][i]:
                    return res
            res += char
        return res