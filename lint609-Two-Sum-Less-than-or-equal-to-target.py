from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        if len(nums) < 2:
            return 0
        res = 0
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                res += right - left
                left += 1
            if nums[left] + nums[right] > target:
                right -= 1
        return res