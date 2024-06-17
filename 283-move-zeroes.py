class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        
        while i < j:
            if nums[j] == 0:
                j -= 1
            if nums[i] == 0:
                k = i
                while k < j:
                    nums[k], nums[k+1] = nums[k+1], nums[k]
                    k += 1
            else:
                i += 1

class SolutionSameDirectionalTwoPointer:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

class SolutionSameDirectionalTwoPointerDecreasedWrite:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1