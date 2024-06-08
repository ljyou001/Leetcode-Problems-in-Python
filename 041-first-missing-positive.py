class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        max_num = max(nums)
        if max_num <= 0:
            return 1
        nums = set(nums)
        for i in range(1, max_num):
            if i not in nums:
                return i
        return max_num + 1 