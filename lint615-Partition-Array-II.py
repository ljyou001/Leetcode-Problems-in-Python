from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums: List[int], low: int, high: int):
        # write your code here
        self.partition(nums, low)
        self.partition(nums, high)

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