class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, si, pi, memo):
        if si == len(s) and pi == len(p):
            return True
        if pi == len(p):
            return False
        # Why no si == len(s)?
        # cuz there could be 0 char match for p
        # say `abc` and `abcd*`
        if (si, pi) in memo:
            return memo[(si, pi)]

        memo[(si, pi)] = False
        
        if pi + 1 < len(p) and p[pi + 1] == '*':
            memo[(si, pi)] = self.dfs(s, p, si, pi + 2, memo)
            # If 0 p[pi] characters
            for i in range(si, len(s)):
                if memo[(si, pi)]:
                    # If already true, don't try to search more
                    break
                if p[pi] != '.' and p[pi] != s[i]:
                    break
                memo[(si, pi)] = self.dfs(s, p, i + 1, pi + 2, memo)
        else:
            if si < len(s) and (s[si] == p[pi] or p[pi] == '.'):
                memo[(si, pi)] = self.dfs(s, p, si + 1, pi + 1, memo)

        return memo[(si, pi)]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i1, i2, memo):
        if i2 == len(p):
            memo[(i1, i2)] = i1 == len(s)
            return memo[(i1, i2)]
        # No need to handle i1 == len(s):
        # For example: s = 'a', p = 'ab*c*d*'
        
        if (i1, i2) in memo:
            return memo[(i1, i2)]
        
        memo[(i1, i2)] = False
        first_match = i1 < len(s) and (p[i2] == s[i1] or p[i2] == '.')

        if i2 + 1 < len(p) and p[i2 + 1] == '*':
            # Handle '?*' case
            # At this case, first_match is to match the i1 + 1 case
            memo[(i1, i2)] = (
                self.dfs(s, p, i1, i2 + 2, memo) 
                or
                (first_match and self.dfs(s, p, i1 + 1, i2, memo))
            ) 
        else:
            # handle non-'?*' case
            memo[(i1, i2)] = first_match and self.dfs(s, p, i1 + 1, i2 + 1, memo)

        return memo[(i1, i2)]