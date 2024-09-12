class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, si, pi, memo):
        if (si, pi) in memo:
            return memo[(si, pi)]
        
        if pi == len(p) and si == len(s):
            return True
        if si == len(s):
            return self.is_all_star(p, pi)
        if pi == len(p):
            return False

        res = False
        if s[si] == p[pi] or p[pi] == '?':
            res = self.dfs(s, p, si + 1, pi + 1, memo)
        elif p[pi] == '*':
            for i in range(si, len(s) + 1):
                res = self.dfs(s, p, i, pi + 1, memo)
                if res:
                    break

        memo[(si, pi)] = res
        return memo[(si, pi)]


    def is_all_star(self, p, pi):
        for i in range(pi, len(p)):
            if p[i] != '*':
                return False
        return True