class DPTypes:
    STEP_ON = 0
    SKIPPED = 1

class SolutionDP:
    # Status transfer:
    # https://onlineboard.eu/b/r0vT3taI
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        dp = [[0] * (2) for _ in range(2)]
        for i in range(len(cost)):
            dp[i % 2][DPTypes.STEP_ON] = cost[i] + min(
                dp[(i - 1) % 2][DPTypes.STEP_ON],
                dp[(i - 1) % 2][DPTypes.SKIPPED],
            )
            dp[i % 2][DPTypes.SKIPPED] = dp[(i - 1) % 2][DPTypes.STEP_ON]

        return min(
            dp[(len(cost) - 1) % 2][DPTypes.STEP_ON],
            dp[(len(cost) - 1) % 2][DPTypes.SKIPPED],
        )

class SolutionMemoOri:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(self.dfs(cost, 0, memo), self.dfs(cost, 1, memo))
    
    def dfs(self, cost, index, memo):
        if index in memo:
            return memo[index]
        
        if index == len(cost) - 1:
            memo[len(cost) - 1] = cost[index]
            return cost[index]
        if index >= len(cost):
            return 0 
            # IN THIS QUESTION:
            # You are allowed to go beyond the top stair
            # If beyond top stair not allowed,
            # You should return float('inf') to block the result

        cost1 = self.dfs(cost, index + 1, memo)
        cost2 = self.dfs(cost, index + 2, memo)
        
        memo[index] = min(cost1, cost2) + cost[index]
        return memo[index]

class SolutionMemo:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        return min(
            self.dfs(cost, 0, memo),
            self.dfs(cost, 1, memo),
        )

    def dfs(self, cost, index, memo):
        if index >= len(cost):
            return 0
        if (index) in memo:
            return memo[index]

        memo[index] = cost[index] + min(
            self.dfs(cost, index + 1, memo),
            self.dfs(cost, index + 2, memo),
        )
        return memo[index]
        