class SolutionMemoSearch:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for source, dest, price in flights:
            if source in graph:
                graph[source].append((dest, price))
            else:
                graph[source] = [(dest, price)]
        
        memo = {}
        res = self.dfs(graph, src, dst, k + 1, memo)
        return res if res != float('inf') else -1

    def dfs(self, graph, src, dst, k, memo):
        if src == dst and k >= 0:
            return 0
        if k < 0 or src not in graph:
            return float('inf')
        
        if (src, k) in memo:
            return memo[(src, k)]
        
        memo[(src, k)] = float('inf')
        for dest, price in graph[src]:
            memo[(src, k)] = min(
                memo[(src, k)],
                self.dfs(graph, dest, dst, k - 1, memo) + price,
            )
        return memo[(src, k)]