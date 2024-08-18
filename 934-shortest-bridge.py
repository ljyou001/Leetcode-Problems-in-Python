DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island = self.find_island(grid)
        res = self.bfs_dist(grid, island) - 1
        return res

    def bfs_dist(self, grid, island):
        visited = {}
        for item in island:
            visited[item] = 0
        queue = deque(island)
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx, newy = x + dx, y + dy
                if not self.is_valid(grid, newx, newy, visited):
                    continue
                if grid[newx][newy] == 0:
                    visited[(newx, newy)] = visited[(x, y)] + 1
                    queue.append((newx, newy))
                elif grid[newx][newy] == 1:
                    return visited[(x, y)] + 1

    def find_island(self, grid):
        island = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not island and grid[i][j] == 1:
                    island = self.bfs(grid, i, j, 1)
                    break
        return island

    def bfs(self, grid, x, y, target):
        queue = deque([(x, y)])
        visited = set([(x, y)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx, newy = x + dx, y + dy
                if not self.is_valid(grid, newx, newy, visited):
                    continue
                if grid[newx][newy] != target:
                    continue
                queue.append((newx, newy))
                visited.add((newx, newy))
        return visited

    def is_valid(self, grid, x, y, visited):
        if not 0 <= x < len(grid):
            return False
        if not 0 <= y < len(grid[0]):
            return False
        if (x, y) in visited:
            return False
        return True