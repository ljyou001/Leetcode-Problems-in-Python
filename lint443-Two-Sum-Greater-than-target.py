from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def two_sum2(self, nums: List[int], target: int) -> int:
        # write your code here
        nums.sort()
        i = 0
        j = len(nums) - 1
        res = 0
        while i < j:
            if nums[i] + nums[j] > target:
                res += j - i
                j -= 1
            else:
                i += 1
        return res