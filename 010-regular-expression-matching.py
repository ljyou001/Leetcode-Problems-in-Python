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