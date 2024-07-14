import heapq

class Solution_sort:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

class Solution_heap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [element * -1 for element in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return heapq.heappop(nums) * -1

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            if len(heap) < k:
                heappush(heap, i)
            elif heap[0] < i:
                heappop(heap)
                heappush(heap, i)
        return heap[0]