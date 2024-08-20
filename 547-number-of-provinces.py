class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                self.bfs(i, isConnected, visited)
                res += 1
        return res

    def bfs(self, start, connect, visited):
        queue = deque([start])
        while queue:
            index = queue.popleft()
            node = connect[index]
            for i in range(len(node)):
                if i in visited:
                    continue
                if not connect[index][i]:
                    continue
                queue.append(i)
                visited.add(i)