class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [
            1 if i > 0 else -1
            for i in nums
        ]
        res = 0
        prefix_sum = 0
        count = {0: -1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum in count:
                res = max(res, i - count[prefix_sum])
            if prefix_sum not in count:
                count[prefix_sum] = i
        return res