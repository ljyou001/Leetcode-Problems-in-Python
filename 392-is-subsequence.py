class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 1:
            return True
        if len(t) < 1:
            return False
        
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1
        print(i)
        return i == len(s)