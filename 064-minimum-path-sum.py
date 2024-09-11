class SolutionDP:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n) for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                    )
                elif i > 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                else:
                    dp[i][j] = grid[i][j]
        
        return dp[m - 1][n - 1]

class SolutionDP:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 0
        dp[1][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i > 0 and j > 0:
                    dp[i][j] = grid[i - 1][j - 1] + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                    )
        
        return dp[m][n]
