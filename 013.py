class Solution:
    def romanToInt(self, s: str) -> int:
        vmap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)-1):
            if vmap[s[i]] < vmap[s[i+1]]:
                res -= vmap[s[i]]
            else:
                res += vmap[s[i]]
        res += vmap[s[-1]]
        return res