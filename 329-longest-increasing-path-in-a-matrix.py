DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class SolutionMemoSearch:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        max_length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                length = self.dfs(matrix, i, j, memo)
                max_length = max(max_length, length)
        return max_length

    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        memo[(x, y)] = 1
        for dx, dy in DIRECTIONS:
            newx, newy = x + dx, y + dy
            if not 0 <= newx < len(matrix) or not 0 <= newy < len(matrix[0]):
                continue
            if not matrix[newx][newy] > matrix[x][y]:
                continue
            memo[(x, y)] = max(
                memo[(x, y)],
                self.dfs(matrix, newx, newy, memo) + 1
            )
        return memo[(x, y)]
