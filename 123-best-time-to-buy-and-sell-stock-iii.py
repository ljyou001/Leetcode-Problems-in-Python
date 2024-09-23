class Status:
    EMPTY1 = 0
    HOLD1 = 1
    EMPTY2 = 2
    HOLD2 = 3
    EMPTY3 = 4

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        dp = [
            [float('-inf')] * 5 
            for _ in range(len(prices) + 1)
        ]
        dp[0][Status.EMPTY1] = 0

        for i in range(len(prices)):
            dp[i + 1][Status.EMPTY1] = 0
            dp[i + 1][Status.HOLD1] = max(
                dp[i][Status.EMPTY1] - prices[i],
                dp[i][Status.HOLD1],
            )
            dp[i + 1][Status.EMPTY2] = max(
                dp[i][Status.HOLD1] + prices[i],
                dp[i][Status.EMPTY2],
            )
            dp[i + 1][Status.HOLD2] = max(
                dp[i][Status.EMPTY2] - prices[i],
                dp[i][Status.HOLD2],
            )
            dp[i + 1][Status.EMPTY3] = max(
                dp[i][Status.HOLD2] + prices[i],
                dp[i][Status.EMPTY3],
            )
        
        return max(
            dp[len(prices)][Status.EMPTY1], 
            dp[len(prices)][Status.EMPTY2], 
            dp[len(prices)][Status.EMPTY3], 
        )