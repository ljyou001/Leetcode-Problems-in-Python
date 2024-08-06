class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        return self.dfs(nums, target, 0, memo)

    def dfs(self, nums, target, index, memo):
        if target == 0 and index == len(nums):
            return 1
        if index >= len(nums):
            return 0
        if (target, index) in memo:
            return memo[(target, index)]
        
        plus = self.dfs(nums, target - nums[index], index + 1, memo)
        minus = self.dfs(nums, target + nums[index], index + 1, memo)
        memo[(target, index)] = plus + minus

        return memo[(target, index)]