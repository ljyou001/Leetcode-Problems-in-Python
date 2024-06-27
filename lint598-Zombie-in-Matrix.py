from typing import (
    List,
)

class Solution:
    def zombie(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        zombie_positions = self.initialize_graph(grid)
        res = -1
        for x, y in zombie_positions:
            self.bfs(grid, x, y)
        min_time = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == float('inf'):
                    return -1
                if grid[row][col] > 0:
                    min_time = max(grid[row][col], min_time)
        return min_time
    
    def initialize_graph(self, grid):
        zombie_positions = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    grid[row][col] = float('inf') # inf human
                elif grid[row][col] == 1:
                    zombie_positions.append((row, col))
                    grid[row][col] = 0 # 1 zombie
                else:
                    grid[row][col] *= -1 # -1 wall
        return zombie_positions
    
    def bfs(self, grid, x, y):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque([(x, y)])
        visited = set([(x, y)])
        time = 0
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx = x + dx
                newy = y + dy
                if not self.is_valid(grid, visited, newx, newy):
                    continue
                if grid[newx][newy] > grid[x][y] + 1:
                    queue.append((newx, newy))
                    grid[newx][newy] = grid[x][y] + 1
                    visited.add((newx, newy))
            
    def is_valid(self, grid, visited, x, y):
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] > 0