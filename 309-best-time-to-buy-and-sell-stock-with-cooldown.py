class StatusTypes:
    COOLDOWN = 0
    JUST_SOLD = -1
    BOUGHT = 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        return max(
            self.dfs(prices, 0, StatusTypes.COOLDOWN, memo),
            self.dfs(prices, 0, StatusTypes.BOUGHT, memo) - prices[0],
        )

    def dfs(self, prices, index, status, memo):
        if index >= len(prices):
            return 0
        if (index, status) in memo:
            return memo[(index, status)]
        
        memo[(index, status)] = 0
        if status == StatusTypes.BOUGHT:
            memo[(index, status)] = max(
                # SELL STOCK
                self.dfs(prices, index + 1, StatusTypes.JUST_SOLD, memo) + prices[index], 
                # DO NOTHING
                self.dfs(prices, index + 1, StatusTypes.BOUGHT, memo), 
            )
        elif status == StatusTypes.COOLDOWN:
            memo[(index, status)] = max(
                # BUY STOCK
                self.dfs(prices, index + 1, StatusTypes.BOUGHT, memo) - prices[index], 
                # DO NOTHING
                self.dfs(prices, index + 1, StatusTypes.COOLDOWN, memo), 
            )
        else:
            memo[(index, status)] = self.dfs(prices, index + 1, StatusTypes.COOLDOWN, memo)
        
        return memo[(index, status)]