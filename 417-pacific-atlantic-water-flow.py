class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_start, atlantic_start = self.find_blocks_by_the_sea(heights)
        pacific, atlantic = deepcopy(pacific_start), deepcopy(atlantic_start)
        for x, y in pacific_start:
            self.bfs(heights, pacific, x, y)
        for x, y in atlantic_start:
            self.bfs(heights, atlantic, x, y)
        return [list(i) for i in list(pacific.intersection(atlantic))]

    def bfs(self, heights, visited, x, y):
        queue = deque([(x, y)])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx, newy = x + dx, y + dy
                if not 0 <= newx < len(heights) or not 0 <= newy < len(heights[0]):
                    continue
                if (newx, newy) in visited:
                    continue
                if heights[newx][newy] < heights[x][y]:
                    continue
                visited.add((newx, newy))
                queue.append((newx, newy))

    def find_blocks_by_the_sea(self, heights):
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        for row in range(m):
            pacific.add((row, 0))
            atlantic.add((row, n - 1))
        for col in range(n):
            pacific.add((0, col))
            atlantic.add((m - 1, col))
        return pacific, atlantic