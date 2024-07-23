class Solution:
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