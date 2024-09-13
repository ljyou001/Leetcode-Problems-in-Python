class Solution:
    def reorganizeString(self, s: str) -> str:
        s = Counter(s)
        heap = []
        for i in s.keys():
            heappush(heap, (-s[i], i))

        res = ''
        while heap:
            times, char = heappop(heap)
            if res and char == res[-1]:
                if not heap:
                    return ''
                times2, char2 = heappop(heap)
                res += char2
                times2 += 1
                if times2 < 0:
                    heappush(heap, (times2, char2))
                heappush(heap, (times, char))
                continue
            
            # if not ==
            res += char
            times += 1
            if times < 0:
                heappush(heap, (times, char))

        return res