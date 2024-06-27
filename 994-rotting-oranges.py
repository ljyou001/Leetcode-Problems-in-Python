class OriginalNodeType:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

class NodeType:
    EMPTY = -1
    FRESH = float('inf') # or > 0
    ROTTEN = 0

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        rottens = self.initialize_graph(grid)
        for x, y in rottens:
            self.bfs(grid, x, y)
        return self.find_result(grid)

    def find_result(self, grid):
        min_time = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == NodeType.FRESH:
                    return -1
                else:
                    min_time = max(min_time, grid[row][col])
        return min_time
        
    def bfs(self, grid, x, y):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque([(x, y)])
        visited = set((x, y))
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
        
    def initialize_graph(self, grid):
        rottens = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == OriginalNodeType.FRESH:
                    grid[row][col] = float('inf')
                elif grid[row][col] == OriginalNodeType.EMPTY:
                    grid[row][col] = -1
                elif grid[row][col] == OriginalNodeType.ROTTEN:
                    grid[row][col] = 0
                    rottens.append((row, col))
        return rottens


class NodeType:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        fresh_oranges = 0
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == NodeType.ROTTEN:
                    queue.append((i, j, 0))  # (x, y, minutes)
                elif grid[i][j] == NodeType.FRESH:
                    fresh_oranges += 1
        
        # BFS
        minutes = 0
        while queue:
            x, y, minutes = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    queue.append((nx, ny, minutes + 1))
        return minutes if fresh_oranges == 0 else -1