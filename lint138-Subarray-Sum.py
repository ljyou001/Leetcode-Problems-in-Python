class Solution:
    def subarray_sum(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        prefix_sums = {0: -1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix in prefix_sums:
                return [prefix_sums[prefix] + 1, i]
            prefix_sums[prefix] = i
        return []