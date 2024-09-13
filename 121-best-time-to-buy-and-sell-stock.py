class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        res = 0
        profit = 0
        while j < len(prices):
            profit = prices[j] - prices[i]
            res = max(res, profit)
            if prices[j] < prices[i]:
                i = j
            j += 1
        return res

class Status:
    HOLD = 1
    CLEAR = 0

class SolutionDP:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * (2) for _ in range(len(prices) + 1)]
        dp[0][Status.CLEAR] = 0
        dp[0][Status.HOLD] = -prices[0]
        res = 0

        for i in range(1, len(prices) + 1):
            dp[i][Status.CLEAR] = max(
                dp[i - 1][Status.CLEAR],
                dp[i - 1][Status.HOLD] + prices[i - 1],
            )
            dp[i][Status.HOLD] = max(
                dp[i - 1][Status.HOLD],
                -prices[i - 1]
            )
        
        return dp[len(prices)][Status.CLEAR]