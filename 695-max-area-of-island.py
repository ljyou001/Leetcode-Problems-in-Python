class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited = set()
        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and (row, col) not in visited:
                    area = max(self.bfs(grid, visited, row, col), area)
        return area
    
    def bfs(self, grid, visited, x, y):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(x, y)])
        visited.add((x, y))
        res = 1
        while queue:
            curx, cury = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx = curx + dx
                newy = cury + dy
                if self.is_valid_island(grid, visited, newx, newy):
                    queue.append((newx, newy))
                    visited.add((newx, newy))
                    res += 1
        return res

    def is_valid_island(self, grid, visited, x, y):
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == 1