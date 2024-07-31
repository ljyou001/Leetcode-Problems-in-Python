class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        res = self.dfs(coins, amount, memo)
        
        return res if res != float('inf') else -1

    def dfs(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if amount in memo:
            return memo[amount]

        memo[amount] = float('inf')
        for i in range(len(coins)):
            memo[amount] = min(memo[amount], self.dfs(
                coins, 
                amount - coins[i],
                memo
            ) + 1)

        return memo[amount]