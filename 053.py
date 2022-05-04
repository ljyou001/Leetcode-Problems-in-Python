class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        sum_list = nums
        
        for i in range(len(nums)-1):
            sum_list[i+1] = max(sum_list[i] + nums[i+1], nums[i+1])
        return max(sum_list)