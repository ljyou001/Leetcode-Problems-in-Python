from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The minimum subscript
    """
    def find_subscript(self, nums: List[int]) -> int:
        nums = [nums[i] - i for i in range(len(nums))]

        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid
            else:
                right = mid
        if nums[left] == 0:
            return left
        if nums[right] == 0:
            return right

        return -1

class SolutionFaster:
    """
    @param nums: An integer array
    @return: The minimum subscript
    """
    def find_subscript(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < mid:
                left = mid
            else:
                right = mid
        if nums[left] == left:
            return left
        if nums[right] == right:
            return right
        return -1