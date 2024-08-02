class SolutionMemoSearch:
    def canPartition(self, nums: List[int]) -> bool:
        sum_num = sum(nums)
        if sum_num % 2 != 0: 
            return False
        target = sum_num // 2
        memo = {}
        return self.dfs(nums, target, 0, memo)
        
    def dfs(self, nums, target, index, memo):
        if target == 0:
            return True
        if target < 0 or index >= len(nums):
            return False
        if (index, target) in memo:
            return memo[(index, target)]

        memo[(index, target)] = self.dfs(
            nums, 
            target - nums[index],
            index + 1,
            memo,
        ) or self.dfs(
            nums, 
            target,
            index + 1,
            memo,
        )
        return memo[(index, target)]

class SolutionDPSet:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        target = sum_nums // 2
        values = set()

        for num in nums:
            for value in list(values):
                if value + num == target:
                    return True
                values.add(value + num)
            if num == target:
                return True
            values.add(num)
        return False
        