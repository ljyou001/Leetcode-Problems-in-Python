class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return []
        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1' and (row, col) not in visited:
                    self.bfs(grid, visited, row, col)
                    islands += 1
        return islands

    def bfs(self, grid, visited, x, y):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            curx, cury = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx = curx + dx
                newy = cury + dy
                if self.is_valid_island(grid, visited, newx, newy):
                    visited.add((newx, newy))
                    queue.append((newx, newy))

    def is_valid_island(self, grid, visited, x, y):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == '1'