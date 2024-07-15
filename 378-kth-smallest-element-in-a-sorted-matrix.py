# Lint 401

class SolutionHeapSolution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            heappush(heap, (matrix[i][0], i, 1))

        res = 0
        for _ in range(k):
            res, list_index, ele_index = heappop(heap)
            if ele_index < len(matrix[list_index]):
                heappush(heap, (
                    matrix[list_index][ele_index], 
                    list_index,
                    ele_index + 1
                ))
        return res