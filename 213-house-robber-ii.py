class SolutionMemoSearch:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}
        return max(
            self.dfs(nums, 0, len(nums) - 2, memo),
            self.dfs(nums, 1, len(nums) - 2, memo),
            self.dfs(nums, 1, len(nums) - 1, memo),
            self.dfs(nums, 2, len(nums) - 1, memo),
        )
    
    def dfs(self, nums, index, end, memo):
        if index > end:
            return 0
        if (index, end) in memo:
            return memo[(index, end)]

        value = 0
        for i in range(index + 2, end + 1):
            value = max(
                value,
                self.dfs(nums, i, end, memo)
            )
        memo[(index, end)] = nums[index] + value
        return memo[(index, end)]