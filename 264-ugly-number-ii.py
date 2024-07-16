class SolutionHeapWithSet:
    def nth_ugly_number(self, n: int) -> int:
        res = 0
        heap = [1]
        visited = set([1])
        for i in range(n):
            res = heappop(heap)
            for prime in (2, 3, 5):
                if res * prime in visited:
                    continue
                heappush(heap, res * prime)
                visited.add(res * prime)
        return res

