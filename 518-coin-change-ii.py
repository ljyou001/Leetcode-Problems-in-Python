class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        return self.dfs(coins, amount, 0, memo)
        
    def dfs(self, coins, amount, index, memo):
        if amount == 0:
            return 1
        if index == len(coins) or amount < 0:
            return 0
        if (amount, index) in memo:
            return memo[(amount, index)]

        memo[(amount, index)] = 0 
        for i in range(index, len(coins)):
            memo[(amount, index)] += self.dfs(
                coins, 
                amount - coins[i],
                i,
                memo,
            )
        return memo[(amount, index)]