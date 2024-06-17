class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for char, count in counter.items():
            heapq.heappush(heap, (-count, char))
        res = ''
        while heap:
            count, char = heapq.heappop(heap)
            res += char * -count
        return res