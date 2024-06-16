from typing import (
    List,
)

class SolutionWithList:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        if not nums:
            return 0
        left_array = []
        for item in nums:
            if item < k:
                left_array.append(item)
        return len(left_array)

class SolutionOnlyCount:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        if not nums:
            return 0
        left_array_length = 0
        for item in nums:
            if item < k:
                left_array_length += 1
        return left_array_length

class SolutionWithArrayPartition:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        if not nums:
            return 0
        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left