class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            for i in range(1, len(nums)):
                while nums[i-1] > nums[i] and i > 0:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    i -= 1

class SolutionPartition:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.partition(nums, 1)
        self.partition(nums, 2)

    def partition(self, nums, pivot):
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1