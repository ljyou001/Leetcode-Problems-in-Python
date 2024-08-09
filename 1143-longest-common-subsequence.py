class SolutionMemoSearch:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.dfs(text1, text2, 0, 0, memo)
        
    def dfs(self, text1, text2, i1, i2, memo):
        if i1 >= len(text1) or i2 >= len(text2):
            return 0
        if (i1, i2) in memo:
            return memo[(i1, i2)]
        
        memo[(i1, i2)] = 0
        if text1[i1] == text2[i2]:
            memo[(i1, i2)] = self.dfs(text1, text2, i1 + 1, i2 + 1, memo) + 1
        else:
            memo[(i1, i2)] = max(
                self.dfs(text1, text2, i1, i2 + 1, memo),
                self.dfs(text1, text2, i1 + 1, i2, memo),
            )
        return memo[(i1, i2)]