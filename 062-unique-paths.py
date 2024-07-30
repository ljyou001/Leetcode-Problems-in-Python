class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if (x, y) == (m - 1, n - 1):
                    continue
                dp[x][y] = dp[x + 1][y] + dp[x][y + 1]
        return dp[0][0]