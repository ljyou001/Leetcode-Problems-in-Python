class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recover_rotated_sorted_array(self, nums: List[int]):
        # write your code here
        if not nums:
            return []
        min_index = 0
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                min_index = i
                break
        if min_index == 0:
            return nums
        
        self.reverse(0, min_index - 1, nums)
        self.reverse(min_index, len(nums) - 1, nums)
        self.reverse(0, len(nums) - 1, nums)

    def reverse(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        