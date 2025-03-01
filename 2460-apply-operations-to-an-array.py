class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                nums[i - 1] *= 2
                nums[i] = 0

        modified_nums = []
        for num in nums:
            if num != 0:
                modified_nums.append(num)
        while len(modified_nums) < len(nums):
            modified_nums.append(0)
        return modified_nums