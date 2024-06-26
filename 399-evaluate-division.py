class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        return [
            self.bfs(graph, query[0], query[1])
            for query in queries
        ]

    def build_graph(self, equations, values):
        graph = {}
        for i in range(len(equations)):
            a, b = equations[i]
            if a in graph:
                graph[a].append((b, values[i]))
            else:
                graph[a] = [(b, values[i])]

            if b in graph:
                graph[b].append((a, 1 / values[i]))
            else:
                graph[b] = [(a, 1 / values[i])]
        return graph
    
    def bfs(self, graph, start, end):
        if start not in graph or end not in graph:
            return -1
        visited, queue = set([start]), deque()
        queue.append((start, 1))
        while queue:
            node, val = queue.popleft()
            if node == end:
                return val
            for n, v in graph[node]:
                if n not in visited:
                    queue.append((n, val * v))
                    visited.add(n)
        return -1