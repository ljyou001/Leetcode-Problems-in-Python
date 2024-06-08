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

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            