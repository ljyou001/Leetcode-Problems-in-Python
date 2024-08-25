class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if obstacleGrid[x][y] == 1:
                    dp[x][y] = 0
                    continue
                if x == m - 1 and y == n - 1:
                    continue
                dp[x][y] = dp[x + 1][y] + dp[x][y + 1]
        return dp[0][0]