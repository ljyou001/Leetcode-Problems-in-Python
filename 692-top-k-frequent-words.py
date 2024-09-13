class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k == 0:
            return []

        words = Counter(words)
        heap = []
        for word in words.keys():
            heapq.heappush(heap, (-words[word], word))
        res = []

        while k > 0:
            times, word = heapq.heappop(heap)
            res.append(word)
            k -= 1
        
        return res