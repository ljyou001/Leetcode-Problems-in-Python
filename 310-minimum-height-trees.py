# LINT 1298

class SolutionTopologicalSort:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph, indegree = self.build_graph(n, edges)
        res = self.topo_sort(n, indegree, graph)
        return res

    def topo_sort(self, n, indegree, graph):
        queue = deque([i for i in range(n) if indegree[i] == 1])
        remaining_nodes = n

        while remaining_nodes > 2:
        # This while loop actually used one of the math property to make judgement
            size = len(queue)
            remaining_nodes -= size
            for _ in range(size):
                node = queue.popleft()
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)
    
    def get_start(self, indegree):
        start = []
        for i in range(len(indegree)):
            if indegree[i] == 1:
                start.append(i)
        return start

    def build_graph(self, n, edges):
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for point in edges:
            graph[point[0]].append(point[1])
            graph[point[1]].append(point[0])
            indegree[point[0]] += 1
            indegree[point[1]] += 1
        return graph, indegree

class SolutionClassicBFSMethod:
    """
    This is the classic BFS method.
    Correct but will over time.
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = self.build_graph(n, edges)
        res = []
        min_height = float('inf')
        for i in range(n):
            height = self.bfs(n, i, graph)
            if height < min_height:
                min_height = height
                res = [i]
            elif height == min_height:
                res.append(i)
        return res

    def bfs(self, n, start, graph):
        height = 0
        queue = deque([start])
        visited = {start: 1}
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited[neighbor] = visited[node] + 1
                height = max(height, visited[node] + 1)
        return height
    
    def build_graph(self, n, edges):
        graph = [[] for _ in range(n)]
        for point in edges:
            graph[point[0]].append(point[1])
            graph[point[1]].append(point[0])
        return graph