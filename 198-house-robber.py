class SolutionIncursionDP:
    def rob(self, nums: List[int]) -> int:
        n1 = 0
        n2 = nums[0]
        
        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            old_n2 = n2
            n2 = max(n1 + nums[i], n2)
            n1 = old_n2

        return n2

class SolutionDFSMemorization:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return max(self.dfs(nums, 0, memo), self.dfs(nums, 1, memo))

    def dfs(self, nums, index, memo):
        if index in memo:
            return memo[index]
        if index >= len(nums):
            return 0
        
        value = 0
        for i in range(index + 2, len(nums)):
            value = max(
                value,
                self.dfs(nums, i, memo)
            )
        
        memo[index] = value + nums[index]
        return memo[index]