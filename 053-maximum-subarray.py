class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        sum_list = nums
        
        for i in range(len(nums)-1):
            sum_list[i+1] = max(sum_list[i] + nums[i+1], nums[i+1])
        return max(sum_list)


# This question has applied the dynamic programming method.
# The idea is to keep track of the maximum sum of subarray ending at each index.
# The maximum sum of subarray ending at index i is the maximum of:
# 1. The sum of the current index i plus the maximum sum of subarray ending at index i-1.
# 2. The current index i.
#
# Let's take an example:
# nums = [1, -2, 3, -2, 4]
#
# sum_list[0] = 1
# Then for sum_list[1], we have the following options:
# 1. sum_list[0] + nums[1] = 1 + (-2) = -1
# 2. nums[1] = -2
# Therefore, sum_list[1] = -1, we choose the biggest one.
#
# Similar to the following cases: we can only choose 
# 1. previous sum list + the current number
# 2. current number
# As required, we need to choose the biggest one.
#
# the 3 essential for dynamic programming:
# 1. function: max(sum_list[i-1] + nums[i], nums[i])
# 2. initialization: sum_list[0] = nums[0]
# 3. termination: until the end of the list
#
# Then we can get the full sum_list=[1, -1, 3, 1, 5]
#
# The final answer is the maximum of sum_list or the last value of the list, if it is bigger.