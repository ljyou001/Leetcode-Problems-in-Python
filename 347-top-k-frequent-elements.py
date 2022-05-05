class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res.keys():
                res[i] = 1
            else:
                res[i] += 1
        res = sorted(res.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(res[i][0])
        return result