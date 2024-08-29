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

class SolutionDP:
    # https://onlineboard.eu/b/UfbLy6EW
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text2[j - 1] == text1[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[len(text1)][len(text2)]

        # WHY CANNOT: ?
        
        # for i in range(1, len(text1) + 1):
        #     for j in range(1, len(text2) + 1):
        #         dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        #         if text2[j - 1] == text1[i - 1]:
        #             dp[i][j] += 1