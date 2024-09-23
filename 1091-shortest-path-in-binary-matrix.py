DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        if grid[0][0] == 1:
            return -1

        queue = collections.deque([(0, 0)])
        visited = {(0, 0): 1}
        while queue:
            x, y = queue.popleft()
            if x == len(grid) - 1 and y == len(grid) - 1:
                return visited[(x, y)]
            for dx, dy in DIRECTIONS:
                newx, newy = x + dx, y + dy
                if not 0 <= newx < len(grid):
                    continue
                if not 0 <= newy < len(grid[0]):
                    continue
                if (newx, newy) in visited:
                    continue
                if grid[newx][newy] == 1:
                    continue
                visited[(newx, newy)] = visited[(x, y)] + 1
                queue.append((newx, newy))
        return -1


from collections import deque

class Solution_slow:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        length = len(grid)
        
        q = deque([(0, 0, 1)])
        visit = [(0,0)]
        while q:
            for _ in range(len(q)):
                row, col, level = q.popleft()
                if row == length-1 and col == length-1:
                    return level
                if row<length-1 and grid[row+1][col] == 0 and (row+1, col) not in visit:
                    q.append((row+1, col, level+1))
                    visit.append((row+1, col))
                if col<length-1 and grid[row][col+1] == 0 and (row, col+1) not in visit:
                    q.append((row, col+1, level+1))
                    visit.append((row, col+1))
                if row>0 and grid[row-1][col] == 0 and (row-1, col) not in visit:
                    q.append((row-1, col, level+1))
                    visit.append((row-1, col))
                if col>0 and grid[row][col-1] == 0 and (row, col-1) not in visit:
                    q.append((row, col-1, level+1))
                    visit.append((row, col-1))
                if row<length-1 and col<length-1 and grid[row+1][col+1] == 0 and (row+1, col+1) not in visit:
                    q.append((row+1, col+1, level+1))
                    visit.append((row+1, col+1))
                if row>0 and col>0 and grid[row-1][col-1] == 0 and (row-1, col-1) not in visit:
                    q.append((row-1, col-1, level+1))
                    visit.append((row-1, col-1))
                if row>0 and col<length-1 and grid[row-1][col+1] == 0 and (row-1, col+1) not in visit:
                    q.append((row-1, col+1, level+1))
                    visit.append((row-1, col+1))
                if row<length-1 and col>0 and grid[row+1][col-1] == 0 and (row+1, col-1) not in visit:
                    q.append((row+1, col-1, level+1))
                    visit.append((row+1, col-1))
        return -1


class Solution_faster:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
        queue = deque([(0, 0, 1)])
        while len(queue) > 0:
            x, y, length = queue.popleft()
            if x < 0 or x >= len(grid):
                continue
            if y < 0 or y >= len(grid):
                continue
            if visited[x][y] == 1:
                continue
            if grid[x][y] == 1:
                continue
            if x == len(grid) - 1 and y == len(grid) - 1:
                if grid[x][y] == 0:
                    return length
                continue
            visited[x][y] = 1
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    queue.append((i, j, length+1))
        return -1