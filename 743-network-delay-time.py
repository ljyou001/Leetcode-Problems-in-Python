class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for src, dest, weight in times:
            if src in graph:
                graph[src].append((dest, weight))
            else:
                graph[src] = [(dest, weight)]

        heap = [(0, k)]
        visited = set()
        t = 0
        while heap:
            dist, source = heapq.heappop(heap)
            if source in visited:
                continue
            visited.add(source)
            t = max(dist, t)
            if source not in graph:
                continue
            for dest, weight in graph[source]:
                heapq.heappush(heap, (weight + dist, dest))
        return t if len(visited) == n else -1