class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 or k == 0:
            return 0
        nums.sort()
        res = nums[k-1] - nums[0]
        for i in range(len(nums) - k + 1):
            res = min(res, nums[i+k-1] - nums[i])
        return res