class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        count = {}
        res = 0
        
        while j < len(s):
            count[s[j]] = count.get(s[j], 0) + 1
            if count[s[j]] > 1:
                res = max(res, j - i)
                i = i + 1
                count = {s[i]: 1}
                j = i
            j += 1
        res = max(res, j - i)
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        hasht = {}
        res = 1
        i = 0
        while i < (len(s)):
            j = i + 1
            while j < len(s):
                if s[j] in s[i:j]:
                    res = max(res, len(s[i:j]))
                    i += 1
                    j = i + 1
                else:
                    res = max(res, len(s[i:j+1]))
                    j += 1
            i += 1
        
        return res