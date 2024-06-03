class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque 
        q = deque()
        l = r = 0
        res = []

        while r < len(nums):
            # maintain a monotonic decreasing queue
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            # if q is too long
            if l > q[0]:
                q.popleft()
            
            # time to collect result
            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res