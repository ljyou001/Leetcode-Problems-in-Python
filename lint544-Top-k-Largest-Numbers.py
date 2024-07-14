import heapq

class Solution:
    def topk(self, nums: List[int], k: int) -> List[int]:
        nums = [i * -1 for i in nums]
        heapq.heapify(nums)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(nums) * -1)
        return res