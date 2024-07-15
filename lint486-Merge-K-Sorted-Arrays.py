# Leet 023
# leet023 is using a linked list
# this one is using array, which means you need to track element index by yourself

import heapq
class SolutionOnlySimpleHeap:
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        array = []
        for i in range(len(arrays)):
            for elem in arrays[i]:
                heapq.heappush(array, elem)
        res = []
        for _ in range(len(array)):
            res.append(heapq.heappop(array))
        return res

import heapq
class SolutionLargeArrays:
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        heap = []

        for i in range(len(arrays)):
            if not arrays[i]:
                continue
            heapq.heappush(heap, (arrays[i][0], i, 1))

        res = []
        while heap:
            value, list_index, ele_index = heapq.heappop(heap)
            res.append(value)
            if ele_index < len(arrays[list_index]):
                heapq.heappush(heap, (
                    arrays[list_index][ele_index],
                    list_index,
                    ele_index + 1,
                ))

        return res