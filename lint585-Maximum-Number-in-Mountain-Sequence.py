from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.is_top(mid, nums) == -1:
                right = mid
            elif self.is_top(mid, nums) == 1:
                left = mid
            else:
                return nums[mid]
        return nums[left] if self.is_top(left, nums) == 0 else nums[right]

    def is_top(self, i, nums):
        if i > 0 and nums[i - 1] > nums[i]:
            return -1
        elif i + 1 < len(nums) and nums[i] < nums[i + 1]:
            return 1
        else:
            return 0