class SolutionMemo:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return self.dfs(s1, s2, s3, 0, 0, memo)

    def dfs(self, s1, s2, s3, i1, i2, memo):
        if i1 == len(s1) and i2 == len(s2):
            memo[(i1, i2)] = True
            return True
        if (i1, i2) in memo:
            return memo[(i1, i2)]

        i3 = i1 + i2
        if i1 < len(s1) and s1[i1] == s3[i3] and \
            self.dfs(s1, s2, s3, i1 + 1, i2, memo):
            return True
        if i2 < len(s2) and s2[i2] == s3[i3] and \
            self.dfs(s1, s2, s3, i1, i2 + 1, memo):
            return True
        memo[(i1, i2)] = False
        return memo[(i1, i2)]